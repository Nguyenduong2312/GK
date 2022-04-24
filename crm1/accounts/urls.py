from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.registerPage,name = 'register'),
    path('login/',views.loginPage,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('products/',views.products,name = 'products'),
    path('customer/<str:pk_test>/',views.customer, name ='customer'),
    path('create_form/<str:pk_test>/',views.createOrder, name = 'createOrder'),
    path('update_form/<str:pk_test>/',views.updateOrder, name = 'updateOrder'),
    path('delete_form/<str:pk_test>/',views.deleteOrder, name = 'deleteOrder'),

]  