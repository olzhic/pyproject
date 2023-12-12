from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
from product.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    product_list = []
    print(type(products))
    for product in products:
        product_list.append(product)
        print(type(product))
    return HttpResponse(
        f"<h1> {product_list[0].name} </h1> \n <h2>{product_list[0].description} </h2> \n <p>{product_list[0].count} </p> \n <p> {product_list[0].date } </p>" )

def json(request):
    products = Product.object

def calculator(request, a, c, b):
    if c == "+":
        return HttpResponse(f"{a+b}")   
    elif c == "-":
        return HttpResponse(f"{a-b}")
    elif c == "divide":
        return HttpResponse(f"{a/b}")
    elif c == "*":
        return HttpResponse(f"{a*b}")

b = random.randint(0, 100)
def guess(request, a):
    if a > b:
        return HttpResponse(f"less ")
    elif a < b:
        return HttpResponse(f"more ")
    elif a == b:
        return HttpResponse("congratulations!")