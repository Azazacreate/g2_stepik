from django.urls import path
from . import views

urlpatterns = [
    path('<int:week_day>', views.get__week_dayInt),
    path('<str:week_day>', views.get__week_day, name='week_days_name')
]
