from django.db import models
from stock.models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticleCession(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='cessions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    date_mise_en_cession = models.DateTimeField(auto_now_add=True)
    actif = models.BooleanField(default=True)  # visible aux collaborateurs

    def __str__(self):
        return f"Cession: {self.article.nom}"

class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ManyToManyField(Article)
    is_validated = models.BooleanField(default=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=[('en_attente', 'En attente'), ('accepté', 'Accepté'), ('refusé', 'Refusé')], default='en_attente')
    def __str__(self):
        return self.user.email

class DemandeSponsoring(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_validated = models.BooleanField(default=True)
    date_demande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=[('en_attente', 'En attente'), ('accepté', 'Accepté'), ('refusé', 'Refusé')], default='en_attente')

    def __str__(self):
        return f"{self.user.username} -> {self.article.article.nom}"



