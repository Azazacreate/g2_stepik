from django.shortcuts import render, get_object_or_404
from .models import Movie

def show__movies(request):
    movies = Movie.objects.all()
    return render(request, 'app_movie/movies.html', context={'movies': movies})

# def show__movie(request, id_movie:int):
#     movie = get_object_or_404(Movie, id=id_movie)
#     return render(request, 'app_movie/movie.html', context={'movie': movie})

def show__movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'app_movie/movie.html', context={'movie': movie})