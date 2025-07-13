from django.db import models

# Create your models here.

class Company(models.Model):
    CATEGORY = [
        ("Commerce", "Commerce"),
        ("Alimentation", "Alimentation"),
        ("Immobilier", "Immobilier")
    ]
    name = models.CharField(max_length=100, blank=False, unique=True)
    category = models.CharField(max_length=100, choices=CATEGORY)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'entreprise {self.name}'