from . import views
from django.urls import path

urlpatterns = [
    path('', views.show__movies),
    path('movie/<int:id_movie>/', views.show__movie, name='movie_detail'),
    # path('movie/<slug:slug_movie>/', views.show__movie, name='movie_detail'),
    path('directors/', views.show__directors),
    path('directors/<int:id_director>/', views.show__director, name='director_detail'),
    path('actors/', views.show__actors),
    path('actors/<int:id_actor>/', views.show__actor, name='actor_detail'),
]
