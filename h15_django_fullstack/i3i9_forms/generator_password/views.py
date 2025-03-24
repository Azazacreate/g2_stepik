from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator_password/home.html')

def generate__password(request):
    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('password_uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('password_numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('password_charactersSpecial'):
        characters.extend(list('!@#$%^&*()'))

    password_length = int(request.GET.get('password_length', default=12))
    for el in range(password_length):
        password += random.choice(characters)
    return render(request, 'generator_password/generate__password.html', context={'password': password})

def about(request):
    return render(request, 'generator_password/about.html')