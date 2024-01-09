from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import Order
from .seria import OrderSerializer
# Create your views here.

#def index(request):
#    order = Order()
#    order.name = 'leshy_loh'
#    order.description = 'spizdily PO3 -a'
#    order.price = 100000
#    order.save()
#    serializer = OrderSerializer(order)
#    return HttpResponse(f'{serializer.data}')

def index(request):
    orders = Order.objects.all()
    order_list = []
    print(type(orders))
    for order in orders:
        order_list.append(order)
        print(type(order))
    return HttpResponse(
        f"<h1> {order_list[0].name} </h1> \n <h2>{order_list[0].description} </h2> \n <p>{order_list[0].price} </p> " )

def index(request):
    products = Order.objects.all()
    return render(request, "index.html", {"products":products})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        order = Order()
        order.name = request.POST.get('name')
        order.description = request.POST.get('description')
        order.price = request.POST.get('price')
        order.save()
    return HttpResponseRedirect('/index')

# изменение данных в бд
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

def delete(request, id):
    try:
        product = Order.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/index')
    except Order.DoesNotExist:
        return HttpResponse('<h1> Product does not exist imbecile </h1>')