from django.db import models
from django.db.models import Avg, Count
from django.utils.translation import gettext_lazy as _
from account.models import FirmProfile


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
    name = models.ForeignKey(FirmProfile, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=CategoryChoices.choices,
        default=CategoryChoices.AUTRE,
        verbose_name=_("Catégorie")
    )
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    website = models.URLField(max_length=200, blank=True, null=True, verbose_name=_("Site Web"))
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("Numéro de téléphone"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    # --- Propriétés pour calculer les statistiques des avis ---

    @property
    def review_count(self):
        """Retourne le nombre total d'avis pour cette entreprise."""
        # 'reviews' vient du related_name dans le modèle Review
        return self.reviews.count()

    @property
    def average_rating(self):
        """Calcule et retourne la note moyenne des avis."""
        # 'reviews' vient du related_name, 'rating' est le champ de note dans Review
        return self.reviews.aggregate(Avg('rating'))['rating__avg'] or 0.0

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Entreprise")
        verbose_name_plural = _("Entreprises")
        ordering = ['name']

