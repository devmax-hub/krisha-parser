from rest_framework import viewsets
from .models import City, Author, Category, Object, Parser, SetFilter
from .serializers import CitySerializer, AuthorSerializer, CategorySerializer, ObjectSerializer, ParserSerializer, SetFilterSerializer
from rest_framework.views import APIView  # Добавлен импорт APIView
from rest_framework.response import Response  # Добавлен импорт Response
from rest_framework import status


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

class ParserViewSet(viewsets.ModelViewSet):
    queryset = Parser.objects.all()
    serializer_class = ParserSerializer

class SetFilterViewSet(viewsets.ModelViewSet):
    queryset = SetFilter.objects.all()
    serializer_class = SetFilterSerializer

class ObjectListView(APIView):
    def get(self, request):
        objects = Object.objects.all()  # Fetch all objects from the database
        serializer = ObjectSerializer(objects, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)
