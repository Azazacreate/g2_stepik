from django.shortcuts import render
from django.http import HttpResponse

def monday(request):
    return HttpResponse('Понедельник.')

def tuesday(request):
    return HttpResponse('''
        <h1>Вторник</h1>
        <p>Список дел:</p>
        <p>1. Пресс качат</p>
        <p>2. Бегит!</p>
    ''')