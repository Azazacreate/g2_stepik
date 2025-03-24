from sqlite3 import register_converter
from django.urls import path, register_converter
from django.http import HttpResponse
from . import views, converters

register_converter(converters.Converter_date, 'y_date')

urlpatterns = [
    path('', views.index),
    path('type/', views.get__types),
    path('type/<str:type_name>', views.get__type, name='type_name'),
    path('<y_date:sign_zodiac>/', views.get__converter_date),
    path('<int:month>/<int:day>/', views.find_out__zodiac),
    path('<int:sign_zodiac>/', views.get__sign_zodiacInt),
    path('<str:sign_zodiac>/', views.get__sign_zodiac, name='horoscope_name'),
]
