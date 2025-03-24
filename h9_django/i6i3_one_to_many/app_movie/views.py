from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from sqlalchemy import nulls_last
from .models import Director, Movie, Actor

def show__movies(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_first=True))
    movies = Movie.objects.annotate(
        fieldNewBool=Value(True),
        fieldNewBoolFalse=Value(False),
        budgetNew=F('budget')+100,
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('name'))
    return render(request, 'app_movie/movies.html', context={
        'movies': movies,
        'agg': agg,
    })

def show__movie(request, id_movie:int):
    movie = get_object_or_404(Movie, id=id_movie)
    return render(request, 'app_movie/movie.html', context={'movie': movie})

# def show__movie(request, slug_movie:str):
#     movie = get_object_or_404(Movie, slug=slug_movie)
#     return render(request, 'app_movie/movie.html', context={'movie': movie})

def show__directors(request):
    directors = Director.objects.all()
    return render(request, 'app_movie/directors.html', context={'directors': directors})

def show__director(request, id_director:int):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'app_movie/director.html', context={'director': director})

def show__actors(request):
    actors = Actor.objects.all()
    return render(request, 'app_movie/actors.html', context={'actors': actors})

def show__actor(request, id_actor:int):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'app_movie/actor.html', context={'actor': actor})
