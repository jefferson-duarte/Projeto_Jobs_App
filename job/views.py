from django.http import HttpResponse
from django.shortcuts import render
from .models import Jobs


def encontrar_jobs(request):
    if request.method == 'GET':
        preco_minimo = request.GET.get('preco_minimo')
        preco_maximo = request.GET.get('preco_maximo')
        

        jobs = Jobs.objects.filter(reservado=False)
        return render(request, 'encontrar_jobs.html', {'jobs': jobs})
    