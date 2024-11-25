from django.urls import path
from .views import platform_view, games_view, cart_view

urlpatterns = [
    path('', platform_view, name='platform'),
    path('games/', games_view, name='games'),
    path('cart/', cart_view, name='cart'),
]