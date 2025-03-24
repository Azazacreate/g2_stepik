from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

week_days_dictInt = {
    1: 'Сегодня 1 день недели',
    2: 'Сегодня 2 день недели',
    3: 'Сегодня 3 день недели',
    4: 'Сегодня 4 день недели',
    5: 'Сегодня 5 день недели',
    6: 'Сегодня 6 день недели',
    7: 'Сегодня 7 день недели',
    21: 'Неверный номер дня - 21',
}
week_days_dict = {
    'monday': 'monday is',
    'tuesday': 'tuesday is',
}

def get__week_daysInt(request, week_days:int):
    description = week_days_dictInt.get(week_days, None)
    if description:
        return HttpResponse(description)

def get__week_days(request, week_days:str):
    description = week_days_dict.get(week_days, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound('HttpResponseNotFound - такого дня недели')