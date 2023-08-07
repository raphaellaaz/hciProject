from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def login(request):
    form=forms.loginFormulario()
    return render(request, 'login.html', {'formLogin':form})

def recover(request):
    form=forms.loginFormulario()
    return render(request, 'recover.html', {'formRecover':form})


def register(request):
    form=forms.UserForm()
    if request.method=='POST':
        usern=request.POST.get('username')
        if request.POST.get('password1') == request.POST.get('password2'):
            passw=request.POST.get('password1')
        else:
            return HttpResponse('Contraseñas no coinciden')
    return render(request, 'register.html', {'formRegister': form })