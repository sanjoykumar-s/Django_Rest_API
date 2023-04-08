from rest_framework import generics
from .models import Breed, Dog
from .serializers import BreedMaker, DogMaker

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'Intro': "Hi! Welcome to the Dog API!",
            'Creator': "This API was created by Sanjoy",
            'Dogs-List': reverse('dog-list', request=request, format=format),
            ##'Dogs-Details': reverse('dog-detail', request=request, format=format),
            'Breeds-List': reverse('breed-list', request=request, format=format),
            ##'Breeds-Details': reverse('breed-detail', request=request, format=format),
        })


class AllBreeds(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedMaker


class SingleBreed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedMaker


class AllDogs(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogMaker


class SingleDog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogMaker
