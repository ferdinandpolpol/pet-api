from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from web.models import Pet
from web.serializers import PetSerializer


def index(request):
    return HttpResponse("Welcome to Pet-API")


class PetAPIView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request):
        name = request.query_params.get('name')
        species = request.query_params.get('species')
        age = request.query_params.get('age')

        filter = dict()
        if name:
            filter["name"] = name
        if species:
            filter["species"] = species
        if age:
            filter["age"] = age

        pets = Pet.objects.filter(**filter)
        serializer = PetSerializer(pets, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
