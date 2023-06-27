from django.urls import path,include 
from . import views,admin 
from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_nested import routers 
router = routers.DefaultRouter()
router.register('cart',views.CartViewSet,basename='cart') 
second = routers.NestedDefaultRouter(router,'cart',lookup='cart')
second.register('item',views.CartItemViewSet,basename='item')
router.register('order',views.OrderViewsSet,basename='order')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(second.urls)),

    # path('main/',views.MainProductViewSet.as_view()),
    path('main/',views.MainProductViewSet.as_view()),
    path('main/<int:id>',views.MainProductViewSet.as_view()),
    path('main/<int:pk>',views.MainProductViewSet.as_view()),
    path('main/brands/',views.BrandViewSet.as_view()),
    path('main/brands/<int:id>',views.BrandViewSet.as_view()),
    # path('main/filter',views.FilterPriceVS.as_view()),
    path('main/men/',views.AllMenViewSet.as_view()),
    path('main/men/<int:id>/',views.AllMenViewSet.as_view()),
    path('main/men/clothes/',views.MenClothesVS.as_view()),
    path('main/men/clothes/<int:id>',views.MenClothesVS.as_view()),
    path('main/men/perfumes/',views.MenPerfumesVS.as_view()),
    path('main/men/perfumes/<int:id>',views.MenPerfumesVS.as_view()),
    path('main/men/accessories/',views.MenAccessoriesVS.as_view()),
    path('main/men/accessories/<int:id>',views.MenAccessoriesVS.as_view()),
    path('main/men/shoes/',views.MenShoesViewSet.as_view()),
    path('main/men/shoes/<int:id>',views.MenShoesViewSet.as_view()),
    #*********************SALES******************************
    path('main/sales/<int:id>',views.SalesViewSet.as_view()),
    path('main/sales/',views.SalesViewSet.as_view()),
    #********************women*******************************
    path('main/women/',views.AllWomenViewSet.as_view()),
    path('main/women/<int:id>',views.AllWomenViewSet.as_view()),   
    path('main/women/clothes/',views.WomenClothesVS.as_view()),   
    path('main/women/clothes/<int:id>',views.WomenClothesVS.as_view()),  
    path('main/women/perfumes/',views.WomenPerfumesVS.as_view()),
    path('main/women/perfumes/<int:id>',views.WomenPerfumesVS.as_view()),
    path('main/women/accessories/',views.WomenAccessoriesVS.as_view()),
    path('main/women/accessories/<int:id>',views.WomenAccessoriesVS.as_view()),
    path('main/women/shoes/',views.WomenShoesViewSet.as_view()),
    path('main/women/shoes/<int:id>',views.WomenShoesViewSet.as_view()),
    # #********************Reviews***********************************
    # path('main/women/<int:id>/reviews/<int:id>',views.ReviewsViewSet.as_view()),
    # path('main/men/<int:id>/reviews/<int:id>',views.ReviewsViewSet.as_view())
    #*******************************carts****************************
    # path('main/cart',views.CartViewSet.as_view()),
    # path('main/cart/<int:pk>',views.CartViewSet.as_view()),
    # path('main/cart/item',views.CartItemViewSet.as_view()),
    # path('main/cart/<int:pk>/item',views.CartItemViewSet.as_view()),
]

