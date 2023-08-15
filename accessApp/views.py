from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from appHCI.models import UserZT
from rest_framework import viewsets
from .serializer import accessAppSerializer
from uuid import *

# Create your views here.

class accessAppView(viewsets.ModelViewSet):
    serializer_class = accessAppSerializer
    queryset = UserZT.objects.all()
    
   

def login(request):
    pass

def register(request):
    pass

def recover(request):
    pass