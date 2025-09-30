from django.shortcuts import render, redirect
from .models import CartItem
from store.models import Product
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404




class CartView(ListView):
    model = CartItem
    template_name = 'cart/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        if(self.request.user.is_anonymous):
            return CartItem.objects.none()
        return CartItem.objects.filter(user=self.request.user)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["grand_totall"] =  CartItem.objects.grand_total(self.request.user)
        return context

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(
            user = request.user,
            product = product,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect("cart_detail")

    


