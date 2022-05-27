from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username').lower().strip()
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect('/auth/cadastro/')
        
        if len(username) == 0 or len(senha.strip()) == 0:
            print(username)
            return redirect('/auth/cadastro/')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            return redirect('/auth/cadastro/')
        
        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            return redirect('/auth/login')
        except:
            return redirect('/auth/cadastro/')


def login(request):
    return HttpResponse('Login')