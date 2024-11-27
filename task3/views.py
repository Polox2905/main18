from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
def platform_view(request):
    return render(request, 'third_task/platform.html')

def games_view(request):
    items = {
        'item1': {'name': 'Atomic heart', 'price': '$10'},
        'item2': {'name': 'CyberPunk 2000', 'price': '$20'},
        'item3': {'name': 'PayDay2', 'price': '$30'}
    }
    context = {'items': items}
    return render(request, 'third_task/games.html', context)


def cart_view(request):
    cart = request.session.get('cart', {})

    items = {
        'item1': {'name': 'Atomic heart', 'price': '$10'},
        'item2': {'name': 'CyberPunk 2000', 'price': '$20'},
        'item3': {'name': 'PayDay2', 'price': '$30'}
    }

    cart_items = {key: {'name': items[key]['name'], 'qty': value} for key, value in cart.items()}
    total_price = sum(int(items[key]['price'][1:]) * qty for key, qty in cart.items() if key in items)

    context = {
        'cart_items': cart_items,
        'items': items,
        'total_price': total_price
    }

    return render(request, 'third_task/cart.html', context)


def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})

    cart[item_id] = cart.get(item_id, 0) + 1

    request.session['cart'] = cart

    return redirect('games')

