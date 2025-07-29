from django.db import models
from account.models import FirmProfile
# Create your models here.

class Companies (models.Model):
    firm = models.ForeignKey(FirmProfile, on_delete =models.CASCADE)