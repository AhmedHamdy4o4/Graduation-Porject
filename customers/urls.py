from django.urls import path 
from . import views 


urlpatterns =[
    path('login',views.register),
    path('main/men/order',views.login),
    path('main/woman/order',views.login),
    path('main/',views.logout)
]