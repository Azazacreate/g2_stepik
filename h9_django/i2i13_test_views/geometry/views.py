from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def get__rectangle_area(request, width: int, height: int):
    data = {'formula_1': f'rectangle = width * height = {int(width) * int(height)}'}
    return render(request, 'geometry/rectangle.html', context=data)

def get__rectangle_area2(request, width, height):
    redirect__url = reverse('rectangle_name', args=(width, height))
    return HttpResponseRedirect(redirect__url)

def get__square_area(request, width: int):
    data = {'formula_2': f'square_area = width ** 2 = {int(width) * int(width)}'}
    return render(request, 'geometry/square.html', context=data)

def get__square_area2(request, width: int):
    return HttpResponseRedirect(f'/calculate__geometry/square/{width}')

def get__circle_area(request, radius: int):
    data = {'formula_3': f'circle_area = radius ** 2 * 3.14 = {int(radius) ** 2 * 3.14}'}
    return render(request, 'geometry/circle.html', context=data)

def get__circle_area2(request, radius: int):
    return HttpResponseRedirect(f'/calculate__geometry/area/{radius}')
