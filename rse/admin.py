from django.contrib import admin
from .models import ArticleCession, DemandeSponsoring, Commande

# Register your models here.
admin.site.register(ArticleCession)
admin.site.register(DemandeSponsoring)
admin.site.register(Commande)