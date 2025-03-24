from . import views
from django.urls import path

urlpatterns = [
    path('', views.show__movies),
    path('movie/<int:id_movie>/', views.show__movie, name='movie_detail'),
    # path('movie/<slug:slug_movie>/', views.show__movie, name='movie_detail'),
]
