from django.urls import path
from .views import ClassBasedView, function_based_view

urlpatterns = [
    path('class-based/', ClassBasedView.as_view(), name='class-based'),
    path('function-based/', function_based_view, name='function-based'),
]