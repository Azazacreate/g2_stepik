from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def get__rectangle_area(request, width: int, height: int):
    return HttpResponse(f'rectangle_area = {int(width) * int(height)}')

def get__rectangle_area2(request, width, height):
    redirect__url = reverse('rectangle_name', args=(width, height))
    return HttpResponseRedirect(redirect__url)

def get__square_area(request, width: int):
    return HttpRespone(f'square_area = {int(width) * int(width)}')

def get__square_area2(request, width: int):
    return HttpResponseRedirect(f'/calculate__geometry/square/{width}')

def get__circle_area(request, radius: int):
    return HttpResponse(f'circle_area = {int(radius) ** 2 * 3.14}')

def get__circle_area2(request, radius: int):
    return HttpResponseRedirect(f'/calculate__geometry/area/{radius}')
