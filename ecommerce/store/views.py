import json

from django.http import JsonResponse
from django.shortcuts import render

from .models import Customer, Order, OrderItem, Product


def _get_order(request):
    """Zwraca otwarte zamówienie zalogowanego klienta albo None dla gościa."""
    if not request.user.is_authenticated:
        return None
    customer, _ = Customer.objects.get_or_create(
        user=request.user,
        defaults={"name": request.user.username, "email": request.user.email},
    )
    order, _ = Order.objects.get_or_create(customer=customer, complete=False)
    return order


def store(request):
    products = Product.objects.all()
    return render(request, "store/store.html", {"products": products})


def cart(request):
    order = _get_order(request)
    items = order.orderitem_set.all() if order else []
    order = order or {"get_cart_total": 0, "get_cart_items": 0}
    return render(request, "store/cart.html", {"items": items, "order": order})


def checkout(request):
    order = _get_order(request)
    items = order.orderitem_set.all() if order else []
    order = order or {"get_cart_total": 0, "get_cart_items": 0}
    return render(request, "store/checkout.html", {"items": items, "order": order})


def updateItem(request):
    if request.method != "POST":
        return JsonResponse({"error": "Metoda niedozwolona"}, status=405)
    order = _get_order(request)
    if order is None:
        return JsonResponse({"error": "Wymagane logowanie"}, status=401)

    data = json.loads(request.body)
    product = Product.objects.get(id=data["productId"])
    item, _ = OrderItem.objects.get_or_create(order=order, product=product)

    if data["action"] == "add":
        item.quantity += 1
    elif data["action"] == "remove":
        item.quantity -= 1

    if item.quantity <= 0:
        item.delete()
    else:
        item.save()
    return JsonResponse({"quantity": max(item.quantity, 0)})
