from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

week_day_dict = {
    'monday': 'Today is monday',
    'tuesday': 'Today is tuesday',
    'wednesday': 'Today is wednesday',
    'thursday': 'Today is thursday',
    'friday': 'Today is friday',
    'saturday': 'Today is saturday',
    'sunday': 'Today is sunday',
}

def get__week_dayInt(request, week_day:int):
    week_days = list(week_day_dict)
    if week_day > len(week_days):
        return HttpResponseNotFound(f'Неправильный номер_дня_недели => {week_day}')
    week_day_name = week_days[week_day - 1]
    redirect_url = reverse('week_days_name', args=(week_day_name, ))
    return HttpResponseRedirect(redirect_url)

def get__week_day(request, week_day:str):
    description = week_day_dict.get(week_day, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound('HttpResponseNotFound - такого дня недели')