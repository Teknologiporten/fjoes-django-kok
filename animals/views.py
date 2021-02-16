from django.shortcuts import render
from .models import *
from .serializers import AnimalSerializer
from .serializers import AnimalTypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AnimalList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnimalDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        animal = self.get_object(pk)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        animal = self.get_object(pk)
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        animal = self.get_object(pk)
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnimalTypeList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        animal_types = AnimalType.objects.all()
        serializer = AnimalTypeSerializer(animal_types, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnimalTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalTypeDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return AnimalType.objects.get(pk=pk)
        except AnimalType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        animal_type = self.get_object(pk)
        serializer = AnimalTypeSerializer(animal_type)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        animal_type = self.get_object(pk)
        animal_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)