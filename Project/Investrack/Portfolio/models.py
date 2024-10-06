# portfolio/models.py

from django.db import models
from django.contrib.auth.models import User

# Modèle Utilisateur (hérité de Django)

# Modèle Portefeuille
class Portefeuille(models.Model):
    nom = models.CharField(max_length=100)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

# Modèle Entreprise
class Entreprise(models.Model):
    nom = models.CharField(max_length=100)
    secteur = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom

# Modèle Investissement
class Investissement(models.Model):
    ACTION = 'Action'
    OBLIGATION = 'Obligation'
    TYPE_CHOICES = [
        (ACTION, 'Action'),
        (OBLIGATION, 'Obligation'),
    ]

    type_investissement = models.CharField(max_length=20, choices=TYPE_CHOICES)
    nombre_actions = models.IntegerField()
    valeur_actuelle = models.DecimalField(max_digits=10, decimal_places=2)
    portefeuille = models.ForeignKey(Portefeuille, on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_actions} de {self.entreprise.nom}'

# Modèle Document Financier
class DocumentFinancier(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to='documents_financiers/')
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Document pour {self.entreprise.nom}'
