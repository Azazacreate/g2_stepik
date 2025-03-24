from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# def monday(request):
#     return HttpResponse('Понедельник.')
#
# def tuesday(request):
#     return HttpResponse('''
#         <h1>Вторник</h1>
#         <p>Список дел:</p>
#         <p>1. Пресс качат</p>
#         <p>2. Бегит!</p>
#     ''')

def get__week_days(request, week_days):
    if week_days == 'monday':
        return HttpResponse('Понедельник')
    elif week_days == 'tuesday':
        return HttpResponse('Вторник')
    else:
        return HttpResponseNotFound('HttpResponseNotFound - такого дня недели')