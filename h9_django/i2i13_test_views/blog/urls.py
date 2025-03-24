from django.urls import path
from . import views

urlpatterns = [
    path('', views.main)
    ,path('posts/', views.posts)
    ,path('posts/<int:number_post>', views.get__number_post)
    ,path('posts/<name_post>/', views.get__name_post)
]