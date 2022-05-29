from django.http import HttpResponse
from django.shortcuts import render


def encontrar_jobs(request):
    return render(request, 'encontrar_jobs.html')