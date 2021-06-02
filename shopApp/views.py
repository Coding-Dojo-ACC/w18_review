from django.shortcuts import render, redirect
from .models import *

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
