from rest_framework import serializers
from .models import City, Author, Category, Object, Parser, SetFilter

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'

class ParserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parser
        fields = '__all__'

class SetFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetFilter
        fields = '__all__'
