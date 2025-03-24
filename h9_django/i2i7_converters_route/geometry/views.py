from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def get__rectangle_area(request, width, height):
    return HttpResponse(f'rectangle_area = {int(width) * int(height)}')

def get__square_area(request, width):
    return HttpResponse(f'square_area = {int(width) * int(width)}')

def get__circle_area(request, radius):
    return HttpResponse(f'circle_area = {int(radius) ** 2 * 3.14}')