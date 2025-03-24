from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/list_detail.html')

def get__name_post(request, name_post):
    data = {'name_post': name_post}
    return render(request, 'blog/detail_by_name.html', context=data)

def get__number_post(request, number_post: int):
    data = {'number_post': number_post}
    return render(request, 'blog/detail_by_number.html', context=data)