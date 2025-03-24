from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<width>/<height>', views.get__rectangle_area)
    ,path('square/<width>', views.get__square_area)
    ,path('circle/<radius>', views.get__circle_area)
]
