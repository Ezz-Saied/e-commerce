from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.

class HomeView(ListView):
    model = Product
    template_name = "store/home.html"
    context_object_name = "products"
    ordering = ['-id']  



class ListProductView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"
    ordering = ['-id']



class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"
    