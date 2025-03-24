from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse('PageMain')

def posts(request):
    return HttpResponse('All posts')