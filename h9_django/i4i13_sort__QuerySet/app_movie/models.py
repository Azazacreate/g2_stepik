from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Director(models.Model):
    name_first = models.CharField(max_length=100, default='режиссер-1')
    last_first = models.CharField(max_length=100, default='режиссер-1')
    director_email = models.EmailField()
    def __str__(self):
        return f'{self.name_first} {self.last_first}'


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = {
        EUR: "Euro",
        USD: "Dollar",
        RUB: "Rubles",
    }
    # id создалось:автоматически
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1_000_000, validators=[MinValueValidator(1)])
    slug = models.SlugField(default='', null=True, db_index=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}, {self.rating}'
    def get__url(self):
        return reverse('movie_detail', args=[self.id])
        # return reverse('movie_detail', args=[self.slug])
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)
