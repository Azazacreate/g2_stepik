from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Movie(models.Model):
    # id создалось:автоматически
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1_000_000)
    slug = models.SlugField(default='', null=False, db_index=True)

    def __str__(self):
        return f'{self.name}, {self.rating}'
    def get__url(self):
        # return reverse('movie_detail', args=[self.id])
        return reverse('movie_detail', args=[self.slug])
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)