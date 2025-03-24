from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<width>/<height>', views.get__rectangle_area)
    ,path('get__rectangle/<width>/<height>', views.get__rectangle_area2, name='rectangle_name')
    ,path('square/<width>', views.get__square_area)
    ,path('get__square/<width>', views.get__square_area2)
    ,path('circle/<radius>', views.get__circle_area)
    ,path('get__circle/<radius>', views.get__circle_area2)
]