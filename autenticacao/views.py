from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return render(request, 'cadastro.html')


def login(request):
    return HttpResponse('Login')