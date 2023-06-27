from django.contrib import admin
from rest_framework.mixins import UpdateModelMixin , CreateModelMixin,ListModelMixin 
from .models import Product ,Order,Review,Customer ,OrderItems,CartItem,Cart
from django.urls import path 
# Register your models here.
# admin.site.site_header("Web Site E commerce")
@admin.register(Product)
class ManageProduct(admin.ModelAdmin):
    list_display= ['description','name','price']
    list_per_page = 15
    list_editable=['price']
    search_fields=['title','name','brand__brand_name']


@admin.register(Review)
class ManageReviews(admin.ModelAdmin):
    list_display = ['product','date','customer','description']

@admin.register(Customer)
class ManageCustomer(admin.ModelAdmin):
    list_display=['name']

@admin.register(OrderItems)
class ManageOrder(admin.ModelAdmin):
    list_display = ['quantity','order','unit_price']

@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    list_display = ['product']

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['date','customer']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['created_at',]



