from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Review, ReviewResponse 
from .serializers import *
from account.models import CustomerProfile, FirmProfile
from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import timezone
from rest_framework.permissions import AllowAny
from core.services import NotificationService

class RecentReviewsAPIView(APIView):
    # Vue pour permettre aux visiteurs d'avoirs accès aux différents avis postés sur le site
    permission_classes = [AllowAny]  # Accès public
    
    def get(self, request):
        # Optimisation pour la Côte d'Ivoire
        reviews = Review.objects.select_related(
            'firm', 
            'customer__user'
        ).order_by('-created_at')[:15]  # 15 derniers avis
        
        serializer = PublicReviewSerializer(reviews, many=True)
        
        return Response({
            'status': 'success',
            'data': serializer.data,
        })

class ReviewAPIView(APIView):

    #Vue reservé aux utilisateurs pour émettre ou supprimer des avis

    permission_classes = [AllowAny]

    def get(self, request, firm_id=None, review_id=None):
        """
        Liste tous les avis d'une entreprise OU un avis spécifique
        """
        if review_id:  # Détail d'un avis
            review = get_object_or_404(Review, id=review_id)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)

        if firm_id:  # Liste des avis pour une entreprise
            firm = get_object_or_404(FirmProfile, id=firm_id)
            reviews = Review.objects.filter(firm=firm).order_by('-created_at')
            serializer = ReviewSerializer(reviews, many=True)
            return Response({
                'firm_name': firm.name,
                'average_rating': firm.average_rating(),
                'reviews': serializer.data
            })

        return Response(
            {"error": "Spécifiez soit firm_id soit review_id"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def post(self, request, firm_id):
        try:
            # Récupération des objets avec gestion d'erreur
            firm = get_object_or_404(FirmProfile, pk=firm_id)
            customer = get_object_or_404(CustomerProfile, user=request.user)
            
            # Vérification des doublons
            if Review.objects.filter(firm=firm, customer=customer).exists():
                return Response(
                    {"error": "Vous avez déjà posté un avis pour cette entreprise"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Création de l'avis
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                # Enregistrer l'avis
                review = serializer.save(firm=firm, customer=customer)

                # Créer une notification pour l'entreprise
                NotificationService.create_notification(
                    user=firm.user,  # L'utilisateur de l'entreprise
                    notification_type='review_posted',
                    message=f"Un nouvel avis a été posté sur votre entreprise {firm.name}.",
                    data={"review_id": review.id, "customer_id": customer.id},
                    target_url=f"/firm/{firm.id}/reviews/{review.id}" # Lien vers l'avis
                )

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, review_id):
        """
        Met à jour un avis existant (seulement par l'auteur)
        """
        review = get_object_or_404(Review, id=review_id)
        customer = get_object_or_404(CustomerProfile, user=request.user)

        if review.customer != customer:
            return Response(
                {"error": "Vous n'êtes pas l'auteur de cet avis"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        """
        Supprime un avis (seulement par l'auteur ou admin)
        """
        review = get_object_or_404(Review, id=review_id)
        customer = get_object_or_404(CustomerProfile, user=request.user)

        if review.customer != customer and not request.user.is_staff:
            return Response(
                {"error": "Action non autorisée"},
                status=status.HTTP_403_FORBIDDEN
            )

        review.delete()
        return Response(
            {"success": "Avis supprimé"}, 
            status=status.HTTP_204_NO_CONTENT
        )
    
class FirmReviewsAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, firm_id):
        """Liste TOUS les avis d'une entreprise"""
        firm = get_object_or_404(FirmProfile, company=firm_id)
        reviews = Review.objects.filter(firm=firm).order_by('-created_at')  # Correction ici
        serializer = PublicReviewSerializer(reviews, many=True)
        
        return Response({
            'firm': firm.company_name,  # Utilisez le bon champ (company_name ou autre)
            'reviews': serializer.data
        })

class ReviewSearchView(APIView):

    #vue pour effectuer les recherches d'avis!

    def get(self, request):
        search_query = request.query_params.get('q', '')
        min_rating = request.query_params.get('min_rating', 0)
        city = request.query_params.get('city', '')
        
        queryset = Review.objects.select_related('firm', 'customer').order_by('-created_at')

        # Construction dynamique du filtre
        filters = Q()
        
        # Texte libre (recherche dans commentaire et nom entreprise)
        if search_query:
            filters &= (
                Q(comment__icontains=search_query) |
                Q(firm__name__icontains=search_query) |
                Q(firm__categories__name__icontains=search_query)
            )
        
        # Filtre par note
        if min_rating:
            filters &= Q(rating__gte=int(min_rating))
        
        # Filtre géographique (ex: "Abidjan")
        if city:
            filters &= Q(firm__city__iexact=city)
        
        # Exécution requête optimisée
        results = queryset.filter(filters).distinct()
        
        # Pagination
        page = self.paginate_queryset(results, request)
        if page is not None:
            serializer = ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = ReviewSerializer(results, many=True)
        return Response(serializer.data)
    
class RespondToReviewAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, review_id):
        try:
            firm_profile = FirmProfile.objects.get(user=request.user)
        except FirmProfile.DoesNotExist:
            return Response({"error": "Utilisateur non autorisé."}, status=status.HTTP_403_FORBIDDEN)

        review = get_object_or_404(Review, id=review_id)

        # Vérifie que l'avis appartient bien à l'entreprise connectée
        if review.firm != firm_profile:
            return Response({"error": "Cet avis ne concerne pas votre entreprise."}, status=status.HTTP_403_FORBIDDEN)

        # Préparer les données
        data = {
            "review": review.id,
            "firm": firm_profile.id,
            "response_text": request.data.get("response_text")
        }

        serializer = ReviewResponseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)