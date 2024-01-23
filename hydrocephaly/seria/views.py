from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from django.http import JsonResponse
from .models import Order
from .seria import OrderSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, "success.html", {})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def index(request): 
    orders = Order.objects.all()
    order_list = []
    print(type(orders))
    for order in orders:
        order_list.append(order)
        print(type(order))
    return HttpResponse(
        f"<h1> {order_list[0].name} </h1> \n <h2>{order_list[0].description} </h2> \n <p>{order_list[0].price} </p> " )

@login_required
def index(request):
    products = Order.objects.all()
    return render(request, "index.html", {"products":products})


# сохранение данных в бд
@login_required
def create(request):
    if request.method == "POST":
        order = Order()
        order.name = request.POST.get('name')
        order.description = request.POST.get('description')
        order.price = request.POST.get('price')
        order.save()
    return HttpResponseRedirect('/index')

# изменение данных в бд
@login_required
def edit(request, id):
    try:
        order = Order.objects.get(id=id)
        if request.method == "POST":
            order.name = request.POST.get('name')
            order.description = request.POST.get('description')
            order.price = request.POST.get('price')
            order.save()
            return HttpResponseRedirect('/index')
        else:
            return render(request, "edit.html", {"prod":order})
    except Order.DoesNotExist:
        return HttpResponse('<h1> Person not found </h1>')
    
@login_required
def delete(request, id):
    try:
        product = Order.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/index')
    except Order.DoesNotExist:
        return HttpResponse('<h1> Product does not exist imbecile </h1>')
    
@login_required
def seria(request, id):
    order = Order.objects.get(id=id)
    serializer = OrderSerializer(order)
    return HttpResponse(f'{serializer.data}')
