from django.shortcuts import render, redirect


# Create your views here.
def platform_view(request):
    return render(request, 'fourth_task/platform.html')


def games_view(request):
    items = [
        {'id': 'item1', 'name': 'Atomic heart', 'price': '$10'},
        {'id': 'item2', 'name': 'CyberPunk 2000', 'price': '$20'},
        {'id': 'item3', 'name': 'PayDay2', 'price': '$30'}
    ]

    context = {
        'items': items,
        'page_title': 'Список игр'
    }
    return render(request, 'fourth_task/games.html', context)


def cart_view(request):
    cart = request.session.get('cart', {})

    # Переносим игры в список
    items = [
        {'id': 'item1', 'name': 'Atomic heart', 'price': '$10'},
        {'id': 'item2', 'name': 'CyberPunk 2000', 'price': '$20'},
        {'id': 'item3', 'name': 'PayDay2', 'price': '$30'}
    ]

    cart_items = []
    total_price = 0

    for item in items:
        if item['id'] in cart:
            cart_items.append({
                'id': item['id'],
                'name': item['name'],
                'qty': cart[item['id']]
            })
            total_price += int(item['price'][1:]) * cart[item['id']]

    context = {
        'cart_items': cart_items,
        'items': items,
        'total_price': total_price
    }

    return render(request, 'fourth_task/cart.html', context)


def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})

    cart[item_id] = cart.get(item_id, 0) + 1

    request.session['cart'] = cart

    return redirect('games')