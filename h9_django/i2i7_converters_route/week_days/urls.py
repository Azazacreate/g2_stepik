from django.urls import path
from . import views

urlpatterns = [
    path('<int:week_days>', views.get__week_daysInt),
    path('<str:week_days>', views.get__week_days)
]

