from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voiture/<int:id>/', views.detail, name='detail'),
    path('ajouter/', views.ajouter, name='ajouter'),
    path('modifier/<int:id>/', views.modifier, name='modifier'),
    path('supprimer/<int:id>/', views.supprimer, name='supprimer'),
]
