from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up_by_html, name='signup-html'),
    path('django_sign_up/', views.sign_up_by_django, name='signup-django'),
]