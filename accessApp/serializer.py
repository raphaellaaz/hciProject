from rest_framework import serializers
from appHCI.models import *

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserZT
        fields='__all__'

class solutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Solucion
        fields='__all__'

class typeSolSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeSol
        fields='__all__'

class negociosSerializer(serializers.ModelSerializer):
    class Meta:
        model=U_Negocios
        fields='__all__'

class typeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeUser
        fields='__all__'

class estadoSolSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstadoSol
        fields='__all__'

class infoSolSerializer(serializers.ModelSerializer):
    class Meta:
        model=InfoSol
        fields='__all__'
        
class suscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Suscritos
        fields='__all__'
        

class trabajaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trabaja
        fields='__all__'

        



