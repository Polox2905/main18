from django.urls import path
from .views import platform_view, games_view, cart_view, add_to_cart

urlpatterns = [
    path('', platform_view, name='platform'),
    path('store/', games_view, name='games'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<slug:item_id>/', add_to_cart, name='add_to_cart'),
]