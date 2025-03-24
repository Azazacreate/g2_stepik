from dask.bag.random import choices
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Director(models.Model):
    name_first = models.CharField(max_length=100, default='режиссер_имя')
    name_last = models.CharField(max_length=100, default='режиссер_фамилия')
    director_email = models.EmailField()
    def __str__(self):
        return f'{self.name_first} {self.name_last}'
    def get__url(self):
        return reverse('director_detail', args=[self.id])


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = {
        MALE: "Мужчина",
        FEMALE: "Женщина",
    }
    name_first = models.CharField(max_length=100, default='актер_имя')
    name_last = models.CharField(max_length=100, default='актер_фамилия')
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.name_first} {self.name_last}'
        else:
            return f'Актриса {self.name_first} {self.name_last}'
    def get__url(self):
        return reverse('actor_detail', args=[self.id])


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
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)
    def __str__(self):
        return f'{self.name}, {self.rating}'
    def get__url(self):
        return reverse('movie_detail', args=[self.id])
        # return reverse('movie_detail', args=[self.slug])
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)
