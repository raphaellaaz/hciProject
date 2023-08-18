from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from appHCI.models import UserZT
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .serializer import loginUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Create your views here.

class loginAppView(viewsets.ModelViewSet):
    serializer_class = loginUserSerializer
    queryset = UserZT.objects.all()
    
    def create(self, request, *args, **kwargs):
        # Hashear la contraseña antes de crear el usuario
        password = request.data.get('password')
        hashed_password = make_password(password)
        request.data['password'] = hashed_password

        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def loginfun(self, request):
        usernam = request.data.get('username')
        passwor = request.data.get('password')

        user = authenticate(username=usernam, password=passwor)

        if user is not None:
            
            return Response({'message':'Acceso Correcto'}, status=status.HTTP_200_OK)
        else:
            
            return Response({'error': 'Credenciales no validas'}, status=status.HTTP_401_UNAUTHORIZED)
   

def loginUserView(APIView):
    def post(self, request):
        usern=request.data.get('username')
        passw=request.data.get('password')

        user= authenticate(username=usern, password=passw)

def registerUserView(APIView):
    def post(self, request, format=None):
        serializer = loginUserSerializer(data=request.data)  # Crea una instancia del serializador con los datos de la solicitud

        if serializer.is_valid():  # Verifica si los datos son válidos según el serializador
            serializer.save()  # Guarda los datos en la base de datos
            return Response({"mensaje": "Registro creado exitosamente."}, status=status.HTTP_201_CREATED)  # Responde con un mensaje de éxito y código de estado 201 (Created)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Responde con los errores de validación y código de estado 400 (Bad Request)

def login(request):
    pass
def recover(request):
    pass