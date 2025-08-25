# account/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from django.conf import settings
import os
import tempfile
import shutil
from PIL import Image
import io

from account.models import CustomerProfile, FirmProfile, PasswordResetToken


class CustomerProfileModelTest(TestCase):
    """Tests pour le modèle CustomerProfile"""
    
    def setUp(self):
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            username='testcustomer',
            email='customer@test.com',
            password='testpass123'
        )
        
        # Création d'un répertoire temporaire pour les médias de test
        self.media_root = tempfile.mkdtemp()
        self.original_media_root = settings.MEDIA_ROOT
        settings.MEDIA_ROOT = self.media_root
        
        # Création d'une image de test
        image = Image.new('RGB', (100, 100), color='red')
        image_file = io.BytesIO()
        image.save(image_file, 'JPEG')
        image_file.seek(0)
        
        self.test_image = SimpleUploadedFile(
            "test_image.jpg",
            image_file.read(),
            content_type="image/jpeg"
        )
    
    def tearDown(self):
        # Nettoyage du répertoire temporaire
        shutil.rmtree(self.media_root)
        settings.MEDIA_ROOT = self.original_media_root
    
    def test_create_customer_profile(self):
        """Test de création d'un profil client"""
        profile = CustomerProfile.objects.create(
            user=self.user,
            phone='+1234567890',
            birth_date='1990-01-01',
            profile_picture=self.test_image
        )
        
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.phone, '+1234567890')
        self.assertIsNotNone(profile.profile_picture)
        self.assertEqual(str(profile), f"Profil Client de {self.user.username}")
    
    def test_profile_picture_resizing(self):
        """Test que l'image de profil est redimensionnée"""
        profile = CustomerProfile.objects.create(
            user=self.user,
            profile_picture=self.test_image
        )
        
        # Vérifier que l'image a été redimensionnée
        with Image.open(profile.profile_picture.path) as img:
            self.assertLessEqual(img.width, 300)
            self.assertLessEqual(img.height, 300)
    
    def test_profile_deletion_deletes_image(self):
        """Test que l'image est supprimée avec le profil"""
        profile = CustomerProfile.objects.create(
            user=self.user,
            profile_picture=self.test_image
        )
        
        image_path = profile.profile_picture.path
        self.assertTrue(os.path.exists(image_path))
        
        # Supprimer le profil
        profile.delete()
        
        # Vérifier que l'image a été supprimée
        self.assertFalse(os.path.exists(image_path))
    
    def test_customer_profile_without_image(self):
        """Test création d'un profil sans image"""
        profile = CustomerProfile.objects.create(
            user=self.user,
            phone='+1234567890'
        )
        
        # Pour les ImageField, on vérifie si le champ est vide (name est None)
        self.assertIsNone(profile.profile_picture.name)
        self.assertEqual(profile.phone, '+1234567890')


class FirmProfileModelTest(TestCase):
    """Tests pour le modèle FirmProfile"""
    
    def setUp(self):
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            username='testfirm',
            email='firm@test.com',
            password='testpass123'
        )
        
        # Création d'un répertoire temporaire pour les médias de test
        self.media_root = tempfile.mkdtemp()
        self.original_media_root = settings.MEDIA_ROOT
        settings.MEDIA_ROOT = self.media_root
        
        # Création d'une image de test
        image = Image.new('RGB', (100, 100), color='blue')
        image_file = io.BytesIO()
        image.save(image_file, 'JPEG')
        image_file.seek(0)
        
        self.test_image = SimpleUploadedFile(
            "test_logo.jpg",
            image_file.read(),
            content_type="image/jpeg"
        )
    
    def tearDown(self):
        # Nettoyage du répertoire temporaire
        shutil.rmtree(self.media_root)
        settings.MEDIA_ROOT = self.original_media_root
    
    def test_create_firm_profile(self):
        """Test de création d'un profil entreprise"""
        profile = FirmProfile.objects.create(
            user=self.user,
            company_name='Test Company',
            address='123 Test Street',
            is_verified=True,
            phone_number='+1234567890',
            company_logo=self.test_image
        )
        
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.company_name, 'Test Company')
        self.assertTrue(profile.is_verified)
        self.assertIsNotNone(profile.company_logo)
        self.assertEqual(str(profile), f"Profil Entreprise de {self.user.username}")
    
    def test_company_logo_resizing(self):
        """Test que le logo est redimensionné"""
        profile = FirmProfile.objects.create(
            user=self.user,
            company_name='Test Company',
            company_logo=self.test_image
        )
        
        # Vérifier que l'image a été redimensionnée
        with Image.open(profile.company_logo.path) as img:
            self.assertLessEqual(img.width, 300)
            self.assertLessEqual(img.height, 300)
    
    def test_firm_profile_deletion_deletes_logo(self):
        """Test que le logo est supprimé avec le profil"""
        profile = FirmProfile.objects.create(
            user=self.user,
            company_name='Test Company',
            company_logo=self.test_image
        )
        
        logo_path = profile.company_logo.path
        self.assertTrue(os.path.exists(logo_path))
        
        # Supprimer le profil
        profile.delete()
        
        # Vérifier que l'image a été supprimée
        self.assertFalse(os.path.exists(logo_path))
    
    def test_firm_profile_without_logo(self):
        """Test création d'un profil entreprise sans logo"""
        profile = FirmProfile.objects.create(
            user=self.user,
            company_name='Test Company',
            address='123 Test Street'
        )
        
        # Pour les ImageField, on vérifie si le champ est vide (name est None)
        self.assertIsNone(profile.company_logo.name)
        self.assertFalse(profile.is_verified)


class PasswordResetTokenModelTest(TestCase):
    """Tests pour le modèle PasswordResetToken"""
    
    def setUp(self):
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            username='testuser',
            email='user@test.com',
            password='testpass123'
        )
    
    def test_create_password_reset_token(self):
        """Test de création d'un token de réinitialisation"""
        expires_at = timezone.now() + timezone.timedelta(hours=1)
        token = PasswordResetToken.objects.create(
            user=self.user,
            expires_at=expires_at
        )
        
        self.assertEqual(token.user, self.user)
        self.assertIsNotNone(token.token)
        self.assertTrue(token.is_valid())
        # La méthode __str__ retourne "Token for username", pas le token lui-même
        self.assertEqual(str(token), f"Token for {self.user.username}")
    
    def test_token_expiration(self):
        """Test que le token expire correctement"""
        # Token expiré
        expired_time = timezone.now() - timezone.timedelta(hours=1)
        expired_token = PasswordResetToken.objects.create(
            user=self.user,
            expires_at=expired_time
        )
        self.assertFalse(expired_token.is_valid())
        
        # Token valide
        valid_time = timezone.now() + timezone.timedelta(hours=1)
        valid_token = PasswordResetToken.objects.create(
            user=self.user,
            expires_at=valid_time
        )
        self.assertTrue(valid_token.is_valid())
    
    def test_unique_token_generation(self):
        """Test que chaque token est unique"""
        expires_at = timezone.now() + timezone.timedelta(hours=1)
        
        token1 = PasswordResetToken.objects.create(
            user=self.user,
            expires_at=expires_at
        )
        
        token2 = PasswordResetToken.objects.create(
            user=self.user,
            expires_at=expires_at
        )
        
        self.assertNotEqual(token1.token, token2.token)


class ModelRelationshipsTest(TestCase):
    """Tests des relations entre modèles"""
    
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@test.com',
            password='testpass123'
        )
        
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@test.com',
            password='testpass123'
        )
    
    def test_one_to_one_relationship_customer(self):
        """Test de la relation OneToOne pour CustomerProfile"""
        customer_profile = CustomerProfile.objects.create(user=self.user1)
        
        # Vérifier la relation directe
        self.assertEqual(customer_profile.user, self.user1)
        
        # Vérifier la relation inverse
        self.assertEqual(self.user1.account_customer_profile, customer_profile)
    
    def test_one_to_one_relationship_firm(self):
        """Test de la relation OneToOne pour FirmProfile"""
        firm_profile = FirmProfile.objects.create(
            user=self.user2,
            company_name='Test Firm'
        )
        
        # Vérifier la relation directe
        self.assertEqual(firm_profile.user, self.user2)
        
        # Vérifier la relation inverse
        self.assertEqual(self.user2.firm_profile, firm_profile)
    
    def test_foreign_key_relationship_password_token(self):
        """Test de la relation ForeignKey pour PasswordResetToken"""
        expires_at = timezone.now() + timezone.timedelta(hours=1)
        token = PasswordResetToken.objects.create(
            user=self.user1,
            expires_at=expires_at
        )
        
        # Vérifier la relation
        self.assertEqual(token.user, self.user1)
        
        # Vérifier qu'un utilisateur peut avoir plusieurs tokens
        token2 = PasswordResetToken.objects.create(
            user=self.user1,
            expires_at=expires_at
        )
        
        self.assertEqual(PasswordResetToken.objects.filter(user=self.user1).count(), 2)