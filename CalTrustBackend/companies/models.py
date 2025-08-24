from django.db import models 
from django.db.models import Avg 
from django.utils.translation import gettext_lazy as _
from account.models import FirmProfile
from django.db.models import Q 
from django.db.models import Count, Case, When, FloatField
from django.core.validators import FileExtensionValidator
import os
from django.conf import settings


class Company(models.Model):
    """
    Modèle représentant une entreprise.
    Les avis sont liés via le modèle 'Review' (non défini ici).
    """

    # --- Définition des choix pour les catégories (meilleure pratique) ---
    class CategoryChoices(models.TextChoices):
        RESTAURATION_HOTELLERIE = 'RH', _('Restauration & Hôtellerie')
        COMMERCE_ECOMMERCE = 'CE', _('Commerce & E-commerce')
        TRANSPORT_LOGISTIQUE = 'TL', _('Transport & Logistique')
        SANTE_BIENETRE = 'SB', _('Santé & Bien-être')
        FINANCE_BANQUE = 'FB', _('Services Financiers & Banques')
        TELECOMS = 'TC', _('Télécommunications')
        EDUCATION_FORMATION = 'EF', _('Éducation & Formation')
        ARTISANAT_SERVICES = 'AS', _('Artisanat & Services Locaux')
        IMMOBILIER = 'IM', _('Immobilier')
        LOISIRS_DIVERTISSEMENT = 'LD', _('Loisirs & Divertissement')
        SERVICES_PUBLICS = 'SP', _('Services Publics & Administration')
        AGROINDUSTRIE = 'AI', _('Agriculture & Agro-industrie')
        AUTRE = 'OT', _('Autre')

    # --- Champs du modèle ---
    name = models.OneToOneField(FirmProfile, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=CategoryChoices.choices,
        default=CategoryChoices.AUTRE,
        verbose_name=_("Catégorie")
    )
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    website = models.URLField(max_length=200, blank=True, null=True, 
                                verbose_name=_("Site Web"),)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))
    
    # --- Documents administratifs PDF ---
    document_1 = models.FileField(
        upload_to='company_documents/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name=_("Document administratif 1"),
        help_text=_("Téléchargez un document PDF (max. 10MB)"),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        max_length=500
    )
    
    document_2 = models.FileField(
        upload_to='company_documents/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name=_("Document administratif 2"),
        help_text=_("Téléchargez un document PDF (max. 10MB)"),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        max_length=500
    )
    
    # Statut de vérification des documents
    documents_verified = models.BooleanField(
        default=False,
        verbose_name=_("Documents vérifiés"),
        help_text=_("Indique si les documents administratifs ont été vérifiés par l'administration")
    )

    # --- Propriétés pour calculer les statistiques des avis ---

    @property
    def review_count(self):
        """Retourne le nombre total d'avis pour cette entreprise."""
        # 'reviews' vient du related_name dans le modèle Review
        return self.reviews.count()
    
    @property
    def reviews(self):
        """Accès aux avis via la relation FirmProfile"""
        return self.name.reviews.all()

    @property
    def average_rating(self):
        """Calcule et retourne la note moyenne des avis, formatée avec une décimale."""
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        if avg_rating is not None:
            # Formate le nombre à une décimale.
            # float(f"{avg_rating:.1f}") assure que même un entier comme 2 devient 2.0
            return float(f"{avg_rating:.1f}")
        return 0.0 # Retourne 0.0 si aucun avis

    @property
    def rating_stats(self):
        """Version corrigée de la méthode stats"""
        reviews = self.name.reviews  # Accès via FirmProfile
        
        stats = reviews.aggregate(
            average=Avg('rating'),
            total=Count('id'),
            stars_5=Count('id', filter=Q(rating=5)),
            stars_4=Count('id', filter=Q(rating=4)),
            stars_3=Count('id', filter=Q(rating=3)),
            stars_2=Count('id', filter=Q(rating=2)),
            stars_1=Count('id', filter=Q(rating=1)),
        )
        
        total = stats['total'] or 0
        if total == 0:
            return {
                'average': 0.0,
                'total': 0,
                'distribution': {'5': 0, '4': 0, '3': 0, '2': 0, '1': 0},
                'percentages': {'5': 0, '4': 0, '3': 0, '2': 0, '1': 0}
            }
        
        return {
            'average': round(stats['average'] or 0, 1),
            'total': total,
            'distribution': {
                '5': stats['stars_5'],
                '4': stats['stars_4'],
                '3': stats['stars_3'],
                '2': stats['stars_2'],
                '1': stats['stars_1'],
            },
            'percentages': {
                '5': round((stats['stars_5'] / total) * 100),
                '4': round((stats['stars_4'] / total) * 100),
                '3': round((stats['stars_3'] / total) * 100),
                '2': round((stats['stars_2'] / total) * 100),
                '1': round((stats['stars_1'] / total) * 100),
            }
        }

    def save(self, *args, **kwargs):
        """Override save pour gérer la suppression des anciens fichiers"""
        # Récupérer l'ancienne instance pour comparer les fichiers
        if self.pk:
            old_instance = Company.objects.get(pk=self.pk)
            
            # Vérifier si document_1 a changé et supprimer l'ancien
            if old_instance.document_1 and old_instance.document_1 != self.document_1:
                if os.path.isfile(old_instance.document_1.path):
                    os.remove(old_instance.document_1.path)
            
            # Vérifier si document_2 a changé et supprimer l'ancien
            if old_instance.document_2 and old_instance.document_2 != self.document_2:
                if os.path.isfile(old_instance.document_2.path):
                    os.remove(old_instance.document_2.path)
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Override delete pour supprimer les fichiers associés"""
        # Supprimer document_1
        if self.document_1:
            if os.path.isfile(self.document_1.path):
                os.remove(self.document_1.path)
        
        # Supprimer document_2
        if self.document_2:
            if os.path.isfile(self.document_2.path):
                os.remove(self.document_2.path)
                
        super().delete(*args, **kwargs)

    @property
    def has_documents(self):
        """Vérifie si l'entreprise a au moins un document"""
        return bool(self.document_1 or self.document_2)

    @property
    def documents_status(self):
        """Retourne le statut des documents"""
        if self.documents_verified:
            return "verified"
        elif self.has_documents:
            return "pending"
        else:
            return "missing"

    @classmethod
    def search(cls, **filters):
        """
        Méthode de recherche avancée
        Exemple d'utilisation: 
        - Company.search(name='resto') → recherche par nom
        - Company.search(category='RH', min_rating=4) → recherche combinée
        """
        queryset = cls.objects.all()
        
        # Filtre par catégorie
        if category := filters.get('category'):
            queryset = queryset.filter(category=category)
            
        # Filtre par terme de recherche (nom ou description)
        if query := filters.get('query'):
            queryset = queryset.filter(
                Q(name__user__username__icontains=query) |
                Q(description__icontains=query)
            )
        
        # Filtre spécifique par nom d'entreprise
        if name := filters.get('name'):
            queryset = queryset.filter(
                Q(name__user__username__icontains=name) |
                Q(name__company_name__icontains=name)
            )
            
        # Filtre par note minimale
        if min_rating := filters.get('min_rating'):
            queryset = queryset.annotate(avg_rating=Avg('reviews__rating'))\
                            .filter(avg_rating__gte=min_rating)
                            
        return queryset.distinct()

    @classmethod
    def get_category_choices(cls):
        """Formatte les choix de catégorie pour l'API"""
        return [{'value': choice[0], 'label': str(choice[1])} 
                for choice in cls.CategoryChoices.choices]
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("Entreprise")
        verbose_name_plural = _("Entreprises")
        ordering = ['name']