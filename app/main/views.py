from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    context = {
        'title':'Home - главная',
        'content':'Магазин техники AlZay',
    }

    return render(request, 'main/index.html', context)

def about (request):
    context = {
        'title':'Home - О нас',
        'content':"Магазин техники AlZay",
        'text_on_page': 'some info',
    }

    return render(request, 'main/about.html', context)
