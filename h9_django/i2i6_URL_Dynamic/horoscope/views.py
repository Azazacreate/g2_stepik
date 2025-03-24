from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# def leo(request):
#     return HttpResponse('Знак_зодиака = лев')
#
# def scorpio(request):
#     return HttpResponse('Знак_зодиака = скорпион')
#
# def aries(request):
#     return HttpResponse('Знак_зодиака = aries')
#
# def taurus(request):
#     return HttpResponse('Знак_зодиака = taurus')

def get__sign_zodiac(request, sign_zodiac):
    if sign_zodiac == 'leo':
        return HttpResponse('Знак_зодиака = лев')
    elif sign_zodiac == 'scorpio':
        return HttpResponse('Знак_зодиака = скорпион')
    elif sign_zodiac == 'aries':
        return HttpResponse('Знак_зодиака = aries')
    elif sign_zodiac == 'taurus':
        return HttpResponse('Знак_зодиака = taurus')
    else:
        return HttpResponseNotFound(f'Знак_зодиака:неизвестный = {sign_zodiac}')