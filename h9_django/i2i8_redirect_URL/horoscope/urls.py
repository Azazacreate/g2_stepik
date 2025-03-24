from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign_zodiac>/', views.get__sign_zodiacInt),
    path('<str:sign_zodiac>/', views.get__sign_zodiac, name='horoscope_name')
]
