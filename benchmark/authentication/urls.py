from django.urls import path
from .views import register

urlpatterns = [
    path('registration', register, name='registration'),
]