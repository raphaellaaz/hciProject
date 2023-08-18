from rest_framework import serializers
from appHCI.models import *

class loginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserZT
        exclude=['id']