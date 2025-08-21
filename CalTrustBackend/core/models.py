from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from account.models import FirmProfile, CustomerProfile
from reviews.models import Review, ReviewResponse
# Create your models here.

class Notifications(models.Model):

    NOTIFICATIONS_TYPES  =(
        ('review_posted', 'Avis posté'),
        ('review_approved', 'Avis approuvé'),
        ('review_rejected', 'Avis rejeté'),
        ('review_responded', 'Avis repondu'),
        ('company_claimed', 'Entreprise réclamée')
    )

    firm = models.ForeignKey(FirmProfile, on_delete = models.CASCADE, related_name = 'notifcations')
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='notifications')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='notifcations')
    review_response = models.ForeignKey(ReviewResponse, on_delete=models.CASCADE, related_name='notifcations')
    notifications_type = models.CharField(max_length=50, choices=NOTIFICATIONS_TYPES)
    message = models.TextField()
    data = models.JSONField(default=dict, blank=True) #Stockage de données sup Ex:image;
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    target_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.firm.company_name} - {self.notifications_type}"