from django.shortcuts import render
from django.http import HttpResponse

def leo(request):
    return HttpResponse('Знак_зодиака = лев')

def scorpio(request):
    return HttpResponse('Знак_зодиака = скорпион')

def aries(request):
    return HttpResponse('Знак_зодиака = aries')

def taurus(request):
    return HttpResponse('Знак_зодиака = taurus')
