from django.contrib import admin
from .models import Product
# Register your models here.
admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "E-Commerce Admin Portal"
admin.site.index_title = "Welcome to E-Commerce Admin Portal"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin) 