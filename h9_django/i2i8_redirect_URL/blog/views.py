from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse('PageMain')

def posts(request):
    return HttpResponse('All posts')

def get__name_post(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')

def get__number_post(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')