from django.urls import path
from .views import hello

urlpatterns = [
    path('', hello, name='hello_world'),   
    path('<str:name>/', hello, name='hello_with_name'),   
]