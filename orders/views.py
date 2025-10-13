from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from cart.models import CartItem
from datetime import date
from django.views.generic import ListView, DetailView


class Check_OutView(LoginRequiredMixin, View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        return render(request, "orders/check_out.html",{
            "cart_items": cart_items,
        })
    
    def post(self, request):
        order = Order(
            user=request.user, 
            date=date.today(), 
            total_price= CartItem.objects.grand_total(user=request.user),
            status="pending"
            )
        order.save()

        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart_items.delete()
        return redirect("success")
    
class SuccessView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "orders/success.html", {
            "order" : Order.objects.filter(user=request.user).last()
        })
       


    
class OrderView(ListView):
    model = Order
    template_name = "orders/orders.html"
    context_object_name = "orders"


class Order_DetailView(DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = self.object.items.all()
        return context
