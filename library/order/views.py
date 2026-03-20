from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm


@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, "order/order_list.html", {"orders": orders})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "order/order_list.html", {"orders": orders})


@login_required
def all_orders(request):
    orders = Order.objects.all()
    return render(request, "order/order_list.html", {"orders": orders})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "order/order_detail.html", {"order": order})


@login_required
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect("order:my_orders")

    else:
        form = OrderForm()

    return render(request, "order/order_create.html", {"form": form})


@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect("order:detail", pk=order.pk)
    else:
        form = OrderForm(instance=order)

    return render(request, "order/order_edit.html", {"form": form, "order": order})


@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        order.delete()
        return redirect("order:index")

    return redirect("order:detail", pk=pk)
