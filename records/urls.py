from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.records, name='records'),
    path('records/details/<id>', views.details, name='details'),
]