from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from sqlalchemy import nulls_last
from .models import Movie

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
