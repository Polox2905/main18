from django.shortcuts import render


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
    context = {}
    return render(request, 'third_task/cart.html', context)