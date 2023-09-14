from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h4>Я поддерживаю я</h4>')

def about():
    return HttpResponse('<h4>Я есть в репозиториях, а ты?</h4>')