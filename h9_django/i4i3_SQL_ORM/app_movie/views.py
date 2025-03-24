from django.shortcuts import render
from .models import Movie

def show__movies(request):
    movies = Movie.objects.all()
    return render(request, 'app_movie/all_movies.html', context={'movies': movies})
