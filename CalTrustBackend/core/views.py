from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage
from .models import Notifications
from .serializer import NotificationsSerializer
from .services import NotificationService

class NotificationPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class NotificationView(APIView):
    """Vue pour gérer les notifications d'un utilisateur"""
    
    permission_classes = [IsAuthenticated]
    pagination_class = NotificationPagination
    
    def get(self, request, *args, **kwargs):
        try:
            # Récupération avec ordering explicite
            notifications = Notifications.objects.filter(
                user=request.user
            ).order_by('-created_at', '-id')
            
            # Filtrage par statut de lecture
            read_status = request.query_params.get('read', None)
            if read_status is not None:
                if read_status.lower() == 'true':
                    notifications = notifications.filter(is_read=True)
                elif read_status.lower() == 'false':
                    notifications = notifications.filter(is_read=False)
            
            # Pagination
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(notifications, request)
            
            if page is not None:
                serializer = NotificationsSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            
            # Fallback si pas de pagination (limite manuelle)
            notifications = notifications[:50]
            serializer = NotificationsSerializer(notifications, many=True)
            
            return Response({
                'notifications': serializer.data,
                'count': notifications.count(),
                'unread_count': NotificationService.get_unread_count(request.user)
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': 'Erreur lors de la récupération des notifications', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class NotificationDetailView(APIView):
    """Vue pour gérer une notification spécifique"""
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, notification_id, *args, **kwargs):
        try:
            notification = Notifications.objects.get(
                id=notification_id, 
                user=request.user
            )
            serializer = NotificationsSerializer(notification)
            return Response(serializer.data)
            
        except Notifications.DoesNotExist:
            return Response(
                {'error': 'Notification non trouvée'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': 'Erreur serveur', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def patch(self, request, notification_id, *args, **kwargs):
        """Marquer une notification comme lue"""
        try:
            success = NotificationService.mark_as_read(notification_id, request.user)
            if success:
                return Response({'status': 'Notification marquée comme lue'})
            else:
                return Response(
                    {'error': 'Notification non trouvée ou accès refusé'},
                    status=status.HTTP_404_NOT_FOUND
                )
                
        except Exception as e:
            return Response(
                {'error': 'Erreur lors de la mise à jour', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class NotificationBulkActionView(APIView):
    """Vue pour les actions groupées sur les notifications"""
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        action = request.data.get('action')
        
        if action == 'mark_all_read':
            NotificationService.mark_all_as_read(request.user)
            return Response({'status': 'Toutes les notifications marquées comme lues'})
        
        elif action == 'clear_all':
            # Attention: suppression définitive
            Notifications.objects.filter(user=request.user, is_read=True).delete()
            return Response({'status': 'Notifications lues supprimées'})
        
        return Response(
            {'error': 'Action non supportée'},
            status=status.HTTP_400_BAD_REQUEST
        )