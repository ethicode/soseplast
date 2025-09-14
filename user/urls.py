from django.urls import path
from . import views


urlpatterns = [
    path('', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('utilisateur/detail/<int:pk>/', views.detail_utilisateur, name='detail_utilisateur'),
]