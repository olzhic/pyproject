from django.shortcuts import render, HttpResponse, HttpResponseRedirect
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


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products":products})

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.save()
    return HttpResponseRedirect('/index')

# изменение данных в бд
def edit(request, id):
    try:
        product = Product.objects.get(id=id)
        if request.method == "POST":
            product.name = request.POST.get('name')
            product.description = request.POST.get('description')
            product.save()
            return HttpResponseRedirect('/index')
        else:
            return render(request, "edit.html", {"prod":product})
    except Product.DoesNotExist:
        return HttpResponse('<h1> Person not found </h1>')

def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/index')
    except Product.DoesNotExist:
        return HttpResponse('<h1> Product does not exist imbecile </h1>')