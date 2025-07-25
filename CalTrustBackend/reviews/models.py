from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import CustomerProfile, FirmProfile

class Review(models.Model):
    firm = models.ForeignKey(
        FirmProfile,
        on_delete=models.CASCADE,
        related_name='reviews',  # Permet d'accéder aux avis via firm.reviews.all()
        verbose_name="Entreprise"
    )
    customer = models.ForeignKey(  # Renommé 'user' en 'customer' pour plus de clarté
        CustomerProfile,
        on_delete=models.CASCADE,
        related_name='reviews',  # Permet d'accéder aux avis via customer.reviews.all()
        verbose_name="Client"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Note"
    )
    comment = models.TextField(verbose_name="Commentaire")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('firm', 'customer')  # Empêche les doublons
        verbose_name = "Avi"
        ordering = ['-created_at']
        # Dans votre modèle Review
        indexes = [
            models.Index(fields=['firm'], name='firm_idx'),
            models.Index(fields=['-created_at'], name='date_desc_idx'),
            #GinIndex(fields=['comment'], name='search_idx')  # Pour PostgreSQL
        ]

    def __str__(self):
        return f"l'utilisateur {self.customer} a noté l'entreprise {self.firm} ({self.rating}/5)"