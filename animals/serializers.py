from rest_framework import serializers
from .models import *

class AnimalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Animal
        fields = '__all__'
    

class AnimalTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnimalType
        fields = '__all__'