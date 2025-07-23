from django.core.mail import EmailMessage
from django.conf import settings
import uuid 
from datetime import timedelta
from django.utils import timezone

def generate_password_reset_token(user):
    """Génère un token sécurisé et le sauvegarde en base"""
    token = uuid.uuid4()
    expires_at = timezone.now() + timedelta(hours=1)
    
    # Import ici pour éviter les dépendances circulaires
    from .models import PasswordResetToken
    
    # Supprime les anciens tokens et crée le nouveau
    PasswordResetToken.objects.filter(user=user).delete()
    PasswordResetToken.objects.create(
        user=user,
        token=token,
        expires_at=expires_at
    )
    return token

def send_password_reset_email(user, reset_link):
    """Envoie un email avec token visible ET bouton cliquable"""
    token = reset_link.split('/')[-1]  # Extrait le token du lien
    subject = "Réinitialisation de votre mot de passe"
    
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 5px;">
            <h2 style="color: #2c3e50;">Réinitialisation du mot de passe</h2>
            
            <!-- Bouton cliquable -->
            <a href="{reset_link}" style="
                display: block; background-color: #3498db; color: white; 
                padding: 12px; text-align: center; border-radius: 4px; 
                margin: 20px 0; text-decoration: none;
            ">
                Réinitialiser mon mot de passe
            </a>
            
            <!-- Token visible pour copier -->
            <div style="background: #eee; padding: 15px; border-radius: 4px;">
                <p style="margin: 0 0 10px 0; font-size: 14px;">
                    Si le bouton ne fonctionne pas, copiez ce code :
                </p>
                <div style="
                    background: white; padding: 10px; font-family: monospace;
                    border: 1px dashed #ccc; text-align: center;
                    font-weight: bold; margin-bottom: 10px;
                ">
                    {token}
                </div>
                <p style="font-size: 12px; color: #666; margin: 0;">
                    Collez-le sur {settings.FRONTEND_URL}/reset-password
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    email = EmailMessage(
        subject,
        html_content,
        settings.EMAIL_HOST_USER,
        [user.email],
    )
    email.content_subtype = "html"
    email.send()