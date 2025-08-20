from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.


User = get_user_model()

class Notifications(models.Model):

    NOTIFICATIONS_TYPES  =(
        ('review_posted', 'Avis posté'),
        ('review_approved', 'Avis approuvé'),
        ('review_rejected', 'Avis rejeté'),
        ('company_claimed', 'Entreprise réclamée')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notifications_type = models.CharField(max_length=50, choices=NOTIFICATIONS_TYPES)
    message = models.TextField()
    data = models.JSONField(default=dict, blank=True) #Stockage de données sup Ex:image;
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    target_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.notifications_type}"