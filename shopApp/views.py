from django.shortcuts import render, redirect
from .models import *
import requests
from django.db.models import Sum

# KEY = '4846bdebaaf6b41115a2e5407e117c66'
# IP = '173.44.109.72'
def index(request):
    allItems = Item.objects.all()
    context = {
        'allItems': allItems,
    }
    return render(request, 'index.html', context)

def addItem(request):
    Item.objects.create(
        itemName=request.POST['itemName'],
        description=request.POST['description'],
        price=request.POST['price'],
    )
    return redirect('/')

def cart(request):
    last = Order.objects.last()
    price=last.totalPrice
    fullOrder = Order.objects.aggregate(Sum('ordered'))['ordered__sum']
    fullPrice = Order.objects.aggregate(Sum('totalPrice'))['totalPrice__sum']
    context = {
        'order': fullOrder,
        'total':fullPrice,
    }
    return render(request, 'cart.html', context)

def purchase(request):
    if request.method == 'POST':
        theItem = Item.objects.filter(id=request.POST['id'])
        if not theItem:
            return redirect('/')
        else:
            quantity = int(request.POST['quantity'])
            total = quantity*(float(theItem[0].price))
            Order.objects.create(
                ordered=quantity,
                totalPrice=total
            )
            return redirect('/cart/')
    else:
        return redirect('/')

def apiData(request):
    allItems = Item.objects.all()
    response = requests.get('https://api.punkapi.com/v2/beers?per_page=1')
    data = response.json()
    print(data)
    return render(request, 'api.html', {
        'data': data,
    })