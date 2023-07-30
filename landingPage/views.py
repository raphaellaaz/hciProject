from django.shortcuts import render, redirect
from django.http import HttpResponse
from appHCI.models import *

# Create your views here.

def cargar(request):
    return render(request,'index.html',{})


def access(request):
    return HttpResponse('Go to hell mthfckr')