from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/auth/plataforma')
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
            messages.add_message(request, constants.ERROR, 'Usuário e senha não podem ficar em branco.')
            return redirect('/auth/cadastro/')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe.')
            return redirect('/auth/cadastro/')
        
        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
            return redirect('/auth/cadastro/')


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/auth/plataforma')
        return render(request, 'logar.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        
        usuario = auth.authenticate(username=username, password=senha)
        
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário não existe.')
            return redirect('/auth/login')
        else:
            auth.login(request, usuario)
            return redirect('/auth/plataforma')
        
        
def sair(request):
    auth.logout(request)
    return redirect('/auth/login')


def plataforma(request):
    return render(request, 'plataforma.html')