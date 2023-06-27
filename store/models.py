from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User 
# Create your models here.
from django.core.validators import MinValueValidator,MaxValueValidator

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name= models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images',null=True)
    def __str__(self):
        return self.brand_name

class Product(models.Model):
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15,decimal_places=2,validators=[MinValueValidator(0)])
    name = models.CharField(max_length=255)
    color=models.CharField(max_length=255,null=True)
    SIZE_LIST = [('L','large'),('M','medium'),('S','small')]
    size = models.CharField(max_length=1,choices=SIZE_LIST,default='L',null=True)
    image = models.ImageField(upload_to='store/images',null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='+')
    type= models.CharField(max_length=255,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    list_of_tuple = [('S','Sales'),('M','Man'),('W','Woman')]
    gender = models.CharField(max_length=1,choices=list_of_tuple,default='M')
    sales = models.BooleanField(default=True,null=True)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default='C')
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE,related_name = 'items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    rate = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    description = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)