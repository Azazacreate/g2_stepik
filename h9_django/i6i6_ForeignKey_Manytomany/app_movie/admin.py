from django.contrib import admin, messages
from django.db.models import QuerySet
from django.core.validators import MinValueValidator, MaxValueValidator
from nltk.corpus import reuters
from openpyxl.styles.builtins import currency
from twisted.conch.insults.insults import modes
from .models import Director, Movie, Actor, RoomDressing


admin.site.register(Director)
admin.site.register(Actor)


# admin.site.register(RoomDressing)
@admin.register(RoomDressing)
class RoomDressing_admin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor',]


class Filter__rating(admin.SimpleListFilter):
    title = 'Filter__rating'
    parameter_name = 'Filter__rating'
    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('40-59', 'Средний'),
            ('60-79', 'High'),
            ('>=80', 'Highest'),
        ]
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        elif self.value() == '40-59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        elif self.value() == '60-79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        elif self.value() == '>=80':
            return queryset.filter(rating__gte=80).filter(rating__lt=100)
        return queryset


# admin.site.register(Movie, Movie_admin)
@admin.register(Movie)
class Movie_admin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug']
    readonly_fields = ['slug']
    # prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'rating', 'director', 'currency', 'year', 'budget']
    list_editable = ['rating', 'director', 'currency', 'year', 'budget']
    ordering = ['-rating', 'year']
    list_per_page = 50  # пагинация
    actions = ['set__dollars', 'set__euro']
    search_fields = ['name']
    list_filter = ['name', 'currency', Filter__rating]
    filter_horizontal = ['actors']


    @admin.display(ordering='rating', description='статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'зачем это смотреть ?'
        elif movie.rating < 70:
            return 'можете-взглянуть разок'
        elif movie.rating <= 85:
            return 'зачет'
        return 'топчиг'

    @admin.action(description='Установить валюту-доллар')
    def set__dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description='Установить валюту-евро')
    def set__euro(self, request, queryset: QuerySet):
        count_updated = queryset.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'обновились {count_updated} записей',
            messages.INFO
        )