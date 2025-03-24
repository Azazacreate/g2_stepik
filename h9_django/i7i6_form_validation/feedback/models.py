from django.db import models
from django.core.validators import MinLengthValidator


class Feedback(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    surname = models.CharField(max_length=50)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()