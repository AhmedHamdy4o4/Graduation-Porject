from django.shortcuts import render,get_object_or_404
from django.db.models import  Q,F
from decimal import Decimal 
from django.db.models import Min,Max
from django_filters.rest_framework import DjangoFilterBackend 
from .models import Product ,Brand ,Category ,Review ,Order,Customer ,Cart ,CartItem
from .serializers import ProductSerializer ,BrandSerializer ,ReviewSerializer,CartSerializer,OrderSerializer,CartItemsSerializer,CreateOrderSerializer,AddCartItemSerializer,SalesSerializer,FilterSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,GenericAPIView,CreateAPIView ,DestroyAPIView,ListAPIView,RetrieveAPIView,RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
# Create your views here.

class MainProductViewSet(ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView,GenericAPIView):
    lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(self,request,*args,**kwargs)
        return self.list(self,request,*args,**kwargs)
    
    queryset = Product.objects.all()
        # filter = self.request.query_params.get('filter')
        # if filter is not None:
        #     if filter=='men':
        #         queryset = queryset.filter(gender='M')
        #     elif filter =='women':
        #         queryset=queryset.filter(gender='W')
    #     # return queryset 
    # def get_serializer_class(self):
    #     if self.request.query_params.get('filter')=='sales':
    serializer_class = ProductSerializer 
    # queryset = Product.objects.all()

class AllMenViewSet(ListAPIView,RetrieveAPIView,GenericAPIView):
    serializer_class = FilterSerializer 
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    queryset =  Product.objects.filter(gender='M').all()

class SalesViewSet(ListAPIView,RetrieveAPIView):
    lookup_field ='id'
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(self,request,*args,**kwargs)
        return self.list(self,request,*args,**kwargs)
    serializer_class = SalesSerializer 
    queryset = Product.objects.all()

class MenClothesVS(ListAPIView,RetrieveAPIView,GenericAPIView):
    serializer_class = ProductSerializer 
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'price':['lt','gt']}
    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    # def get_queryset(self):
    #     if self.request.method =='POST':
    #         fmax = Product.objects.all().aggregate(Max('price'))['price__max']
    #         fmin = Product.objects.all().aggregate(Min('price'))['price__min']
    #         F_Max = self.request.GET.get('MinPrice')
    #         F_Min = self.request.GET.get('MaxPrice')
            
    #         if F_Max is not None and F_min is not None:
    #             if F_max > fmax:
    #                 F_max = fmax 
    #             if F_Min<fmin:
    #                 F_Min = fmin 
    #             queryset = Product.objects.filter(price__range=(F_min,F_max))
    #             return queryset
    queryset = Product.objects.filter(category__id=1).filter(gender='M').all()

class MenPerfumesVS(ListAPIView,RetrieveAPIView,GenericAPIView):
    serializer_class = ProductSerializer 
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'price':['lt','gt']}
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def get_queryset(self):
        if self.request.method =='POST':
            fmax = Product.objects.all().aggregate(Max('price'))['price__max']
            fmin = Product.objects.all().aggregate(Min('price'))['price__min']
            F_Max = self.request.GET.get('MinPrice')
            F_Min = self.request.GET.get('MaxPrice')
            
            if F_Max is not None and F_min is not None:
                if F_max > fmax:
                    F_max = fmax 
                if F_Min < fmin:
                    F_Min = fmin 
                queryset = Product.objects.filter(price__range=(F_min,F_max))
                return queryset
        return Product.objects.filter(category__id=2).filter(gender='M').all()

class MenAccessoriesVS(ListAPIView,RetrieveAPIView,GenericAPIView):
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'price':['lt','gt']}
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def get_queryset(self):
        if self.request.method =='POST':
            fmax = Product.objects.all().aggregate(Max('price'))['price__max']
            fmin = Product.objects.all().aggregate(Min('price'))['price__min']
            F_Max = self.request.GET.get('MinPrice')
            F_Min = self.request.GET.get('MaxPrice')
            
            if F_Max is not None and F_min is not None:
                if F_max > fmax:
                    F_max = fmax 
                if F_Min<fmin:
                    F_Min = fmin 
                queryset = Product.objects.filter(price__range=(F_min,F_max))
                return queryset
        return Product.objects.filter(category__id=3).filter(gender='M').all()
    serializer_class = ProductSerializer 

class MenShoesViewSet(ListAPIView,RetrieveAPIView):
    lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(self,request,*args,**kwargs)
        return self.list(self,request,*args,**kwargs)
    queryset = Product.objects.filter(category__id=4).filter(gender='M')
    serializer_class = ProductSerializer

class BrandViewSet(ListAPIView,RetrieveAPIView,GenericAPIView):
    lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

#*************************women classes ********************

class AllWomenViewSet(ListCreateAPIView,RetrieveAPIView,GenericAPIView):
    lookup_field = 'id'
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = {'price':['lt','gt']}
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    # def get_queryset(self):
    #     if self.request.method =='POST':
    #         fmax = Product.objects.all().aggregate(Max('price'))['price__max']
    #         fmin = Product.objects.all().aggregate(Min('price'))['price__min']
    #         F_Max = self.request.GET.get('MinPrice')
    #         F_Min = self.request.GET.get('MaxPrice')
            
    #         if F_Max is not None and F_min is not None:
    #             if F_max > fmax:
    #                 F_max = fmax 
    #             if F_Min<fmin:
    #                 F_Min = fmin 
    #             queryset = Product.objects.filter(price__range=(F_min,F_max))
    #             return queryset
        
    queryset = Product.objects.filter(gender='W').all()
    serializer_class = FilterSerializer 
class WomenClothesVS(ListAPIView,RetrieveAPIView,GenericAPIView):
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'price':['lt','gt']}
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def get_queryset(self):
        if self.request.method =='POST':
            fmax = Product.objects.all().aggregate(Max('price'))['price__max']
            fmin = Product.objects.all().aggregate(Min('price'))['price__min']
            F_Max = self.request.GET.get('MinPrice')
            F_Min = self.request.GET.get('MaxPrice')
            
            if F_Max is not None and F_min is not None:
                if F_max > fmax:
                    F_max = fmax 
                if F_Min<fmin:
                    F_Min = fmin 
                queryset = Product.objects.filter(price__range=(F_min,F_max))
                return queryset
        return Product.objects.filter(category__id=1).filter(gender='W').all()
    serializer_class = ProductSerializer 

class WomenPerfumesVS(ListAPIView,RetrieveAPIView,GenericAPIView):
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'price':['lt','gt']}
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
        
    def get_queryset(self):
        if self.request.method =='POST':
            fmax = Product.objects.all().aggregate(Max('price'))['price__max']
            fmin = Product.objects.all().aggregate(Min('price'))['price__min']
            F_Max = self.request.GET.get('MinPrice')
            F_Min = self.request.GET.get('MaxPrice')

            if F_Max is not None and F_min is not None:
                if F_max > fmax:
                    F_max = fmax 
                if F_Min<fmin:
                    F_Min = fmin 
                queryset = Product.objects.filter(price__range=(F_min,F_max))
                return queryset
        return Product.objects.filter(category__id=2).filter(gender='W').all()
    serializer_class = ProductSerializer 

class WomenAccessoriesVS(ListAPIView,RetrieveAPIView):
    serializer_class = ProductSerializer 
    lookup_field='id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'price':['lt','gt']}
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    def get_queryset(self):
        if self.request.method =='POST':
            fmax = Product.objects.all().aggregate(Max('price'))['price__max']
            fmin = Product.objects.all().aggregate(Min('price'))['price__min']
            F_Max = self.request.GET.get('MinPrice')
            F_Min = self.request.GET.get('MaxPrice')
            
            if F_Max is not None and F_min is not None:
                if F_max > fmax:
                    F_max = fmax 
                if F_Min<fmin:
                    F_Min = fmin 
                queryset = Product.objects.filter(price__range=(F_min,F_max))
                return queryset
        return Product.objects.filter(category__id=3).filter(gender='W').all()

class WomenShoesViewSet(ListAPIView,RetrieveAPIView):
    lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(self,request,*args,**kwargs)
        return self.list(self,request,*args,**kwargs)    
    queryset = Product.objects.filter(category__id=4).filter(gender='W')
    serializer_class = ProductSerializer
# class FilterPriceVS(ListCreateAPIView,RetrieveUpdateAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         if self.request.method =='POST':
#             fmax = Product.objects.all().aggregate(Max('price'))['price__max']
#             fmin = Product.objects.all().aggregate(Min('price'))['price__min']
#             F_Max = self.request.GET.get('MinPrice')
#             F_Min = self.request.GET.get('MaxPrice')
            
#             if F_Max is not None and F_min is not None:
#                 if F_max > fmax:
#                     F_max = fmax 
#                 if F_Min<fmin:
#                     F_Min = fmin 
#                 queryset = Product.objects.filter(price__range=(F_min,F_max))
#                 return queryset
        
#         return Product.objects.all()

# class ReviewsViewSet(ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView,GenericAPIView):  
#     serializer_class = ReviewSerializer 
#     lookup_field = 'id'
#     def get(self,request,*args,**kwargs):
#         if 'id' in kwargs:
#             return self.retrieve(self,*args,**kwargs)
#         return self.list(self,*args,**kwargs)
#     def get_serializer_context(self):
#         return {'product_id':"product_id"}

    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         return Review.objects.all()
    #     (customer_id,created) = Customer.objects.only('id').get_or_create(user_id=self.request.user.id) #return id of current user
    #     queryset = Review.objects.filter(customer_id=customer_id)
    #     return queryset

#**********************carts*****************

class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method=='POST':
            return AddCartItemSerializer
        return CartItemsSerializer

    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}
    
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')

#******************Orders**************************************
class OrderViewsSet(ModelViewSet):
    def get_serializer_context(self):   
        return {'user_id':self.request.user.id}
    def create(self,request,*args,**kwargs):
        serializer = CreateOrderSerializer(data=request.data , context={'user_id':self.request.user.id}) 
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    def get_serializer_class(self):
        if self.request.method =='POST':
            return CreateOrderSerializer
        return OrderSerializer  
    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()                       #this for exception
        (customer,created) = Customer.objects.only('id').get_or_create(id=self.request.user.id) #return id of current user
        queryset= Order.objects.filter(customer_id=id)
        return queryset