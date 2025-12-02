from django.urls import path
from .views import index, about, features, team

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('features/', features, name='features'),
    path('team/', team, name='team'),
]
