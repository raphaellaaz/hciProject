from django.shortcuts import render
from django.http import HttpResponse
from appHCI.models import *
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Create your views here.

class userAppView(viewsets.ModelViewSet):
    serializer_class = userSerializer
    queryset = UserZT.objects.all()
    
    def create(self, request, *args, **kwargs):
        # Hashear la contraseña antes de crear el usuario
        password = request.data.get('password')
        hashed_password = make_password(password)
        request.data['password'] = hashed_password

        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['get'],url_path='(?P<username>[^/.]+)')
    def readOne(self, request, username=None):
        try:
            userInfo=get_object_or_404(UserZT, username=username)

            serializer = self.get_serializer(userInfo)
            return Response({'user':serializer.data, 'message': 'USer OK'}, status=status.HTTP_200_OK)
        
        except UserZT.DoesNotExist:
            return Response({'message': 'No se ha encontrado usuario'}, status=status.HTTP_404_NOT_FOUND)
        

    @action(detail=False, methods=['post'])
    def loginfun(self, request):
        usernam = request.data.get('username')
        passwor = request.data.get('password')

        user = authenticate(username=usernam, password=passwor)

        if user is not None:
            return Response({'message':'Acceso Correcto'}, status=status.HTTP_200_OK)
        else:
            
            return Response({'error': 'Credenciales no validas'+str(passwor)}, status=status.HTTP_401_UNAUTHORIZED)
   

class solutionsAppView(viewsets.ModelViewSet):
    serializer_class = solutionsSerializer
    queryset = Solucion.objects.all()

class typeSolAppView(viewsets.ModelViewSet):
    serializer_class = typeSolSerializer
    queryset = TypeSol.objects.all()

class negociosAppView(viewsets.ModelViewSet):
    serializer_class = negociosSerializer    
    queryset = U_Negocios.objects.all()
class typeUserAppView(viewsets.ModelViewSet):
    serializer_class = typeUserSerializer
    queryset = TypeUser.objects.all()

class estadoSolAppView(viewsets.ModelViewSet):
    serializer_class = estadoSolSerializer
    queryset = EstadoSol.objects.all()

class infoSolAppView(viewsets.ModelViewSet):
    serializer_class = infoSolSerializer
    queryset = InfoSol.objects.all()

class suscritosAppView(viewsets.ModelViewSet):
    serializer_class = suscritosSerializer
    queryset = Suscritos.objects.all()

    @action(detail=False, methods=['get'],url_path='(?P<idsol>[^/.]+)')
    def sus(self,request, idsol=None):
        try:
            solInfo=get_object_or_404(Solucion, id=idsol)
            susInfo=Suscritos.objects.filter( id_solution=solInfo.id)
            countInfo=susInfo.count()
            userInfos=[]

            for sus in susInfo:
                user=UserZT.objects.get(id=sus.id_user.id)
                user.password='Restringed';
                userInfos.append(user)

            serializerUser = userSerializer(userInfos, many=True)
            return Response({'users':serializerUser.data}, status=status.HTTP_200_OK)
        
        
        except UserZT.DoesNotExist:
            return Response({'message': 'No se ha registro o existe algun error'}, status=status.HTTP_404_NOT_FOUND)

class trabajaAppView(viewsets.ModelViewSet):
    serializer_class = trabajaSerializer
    queryset = Trabaja.objects.all()



