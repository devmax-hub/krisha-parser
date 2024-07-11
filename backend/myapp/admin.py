from django.contrib import admin
from .models import City, Author, Category, Object, Parser, SetFilter

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('url', 'room', 'square', 'city', 'description', 'photo')
    search_fields = ('city', 'description')

@admin.register(Parser)
class ParserAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    list_filter = ('status',)

@admin.register(SetFilter)
class SetFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'filter_json')
    search_fields = ('name', 'filter_json')
