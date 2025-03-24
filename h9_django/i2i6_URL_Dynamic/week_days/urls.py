from django.urls import path
from . import views

urlpatterns = [
    path('<week_days>', views.get__week_days)
    # ,path("monday/", views.monday)
    # ,path("tuesday/", views.tuesday)
]

