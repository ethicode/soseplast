from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.ArticleListView.as_view(), name='article-list'),
# ]



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('articles/', views.liste_articles, name='liste_articles'),
    path('articles/ajouter/', views.ajouter_article, name='ajouter_article'),
    # path('articles/modifier/<int:pk>/', views.modifier_article, name='modifier_article'),
    path('articles/detail/<int:pk>/', views.detail_article, name='detail_article'),
    # path('articles/supprimer/<int:pk>/', views.supprimer_article, name='supprimer_article'),
]