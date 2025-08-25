from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from account.models import CustomerProfile, FirmProfile

class Review(models.Model):
    firm = models.ForeignKey(
        FirmProfile,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Entreprise"
    )
    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Client"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Note"
    )
    comment = models.TextField(verbose_name="Commentaire")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Nouveaux champs pour le système de like
    useful_count = models.PositiveIntegerField(default=0, verbose_name="Nombre de votes utiles")
    users_who_found_useful = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='UsefulVote',
        related_name='useful_reviews',
        blank=True,
        verbose_name="Utilisateurs ayant trouvé l'avis utile"
    )

    class Meta:
        unique_together = ('firm', 'customer')
        verbose_name = "Avi"
        verbose_name_plural = "Avis"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['firm'], name='firm_idx'),
            models.Index(fields=['-created_at'], name='date_desc_idx'),
        ]
    
    def __str__(self):
        return f"l'utilisateur {self.customer} a noté l'entreprise {self.firm} ({self.rating}/5)"
    
    def toggle_useful_vote(self, user):
        """Ajoute ou retire un vote utile"""
        already_voted = self.users_who_found_useful.filter(id=user.id).exists()
        
        if already_voted:
            self.users_who_found_useful.remove(user)
            self.useful_count -= 1
            action = "removed"
        else:
            self.users_who_found_useful.add(user)
            self.useful_count += 1
            action = "added"
        
        self.save()
        return action, self.useful_count
    
    def has_user_voted(self, user):
        """Vérifie si un utilisateur a voté pour cet avis"""
        if user.is_authenticated:
            return self.users_who_found_useful.filter(id=user.id).exists()
        return False

class UsefulVote(models.Model):
    """Modèle intermédiaire pour gérer les votes utiles"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur"
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name="Avis",
        related_name='useful_votes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'review')
        verbose_name = "Vote utile"
        verbose_name_plural = "Votes utiles"
        indexes = [
            models.Index(fields=['user', 'review'], name='user_review_vote_idx'),
        ]
    
    def __str__(self):
        return f"{self.user.username} a trouvé l'avis #{self.review.id} utile"

class ReviewResponse(models.Model):
    review = models.OneToOneField(
        'Review',
        on_delete=models.CASCADE,
        related_name='response',
        verbose_name="Avis concerné"
    )
    firm = models.ForeignKey(
        'account.FirmProfile',
        on_delete=models.CASCADE,
        verbose_name="Entreprise répondante"
    )
    response_text = models.TextField(verbose_name="Réponse de l'entreprise")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Réponse à un avis"
        verbose_name_plural = "Réponses aux avis"
        ordering = ['-created_at']

    def __str__(self):
        return f"Réponse de {self.firm.company_name} à l'avis #{self.review.id}"