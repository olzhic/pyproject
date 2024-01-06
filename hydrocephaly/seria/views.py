from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import Order
from .seria import OrderSerializer
# Create your views here.

def index(request):
    order = Order()
    order.name = 'leshy_loh'
    order.description = 'spizdily PO3 -a'
    order.price = 100000
    order.save()
    serializer = OrderSerializer(order)

    return HttpResponse(f'{serializer.data}')
    
