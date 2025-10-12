from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from cart.models import CartItem
from datetime import date

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
        return redirect("home")