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
        verbose_name = "Avis"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer} → {self.firm} ({self.rating}/5)"