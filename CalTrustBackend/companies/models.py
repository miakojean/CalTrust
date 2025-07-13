from django.db import models

# Create your models here.

class Company(models.Model):
    CATEGORY = [
        ("Commerce", "Commerce"),
        ("Alimentation", "Alimentation"),
        ("Immobilier", "Immobilier")
    ]
    name = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY)

    def __str__(self):
        return f'entreprise {self.name} de la catégorie {self.category}'