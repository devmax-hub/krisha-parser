from django.urls import path
from .views import ObjectListView

urlpatterns = [
    path('objects/', ObjectListView.as_view(), name='object-list'),
]
