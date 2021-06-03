from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addItem/', views.addItem),
    path('cart/', views.cart),
    path('purchase/', views.purchase),
    path('api/', views.apiData),
]