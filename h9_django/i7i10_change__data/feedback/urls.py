from django.contrib import admin
from django.urls import path
from .views import index, done, change__feedback

urlpatterns = [
    path("done", done),
    path("", index),
    path("<int:id_feedback>", change__feedback),
]