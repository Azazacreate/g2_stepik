from django.urls import path
from generator_password import views

urlpatterns = [
    path("", views.home, name='home'),
    path("generate__password/", views.generate__password, name='password'),
    path("about/", views.about, name='about'),
]
