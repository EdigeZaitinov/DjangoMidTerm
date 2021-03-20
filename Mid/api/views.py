from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Journal,BookJournalBase


def home(request):
    return HttpResponse("<h1>Привет мир<h1>")


def main(request):
    return HttpResponse('<h1>Main<h1>')

def books(request):
    data=Book.objects.all()
    return render(request,'api/books.html',context={"books":data})

def journals(request):
    data=Journal.objects.all()
    return render(request,'api/journals.html',context={"journals":data})

def login(request):
    return HttpResponse('<h1>Login<h1>')

def register(request):
   return HttpResponse('<h1>Register<h1>')
