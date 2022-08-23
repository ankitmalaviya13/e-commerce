from app_seller import views
from django.urls import  path

urlpatterns = [
    path('',views.index_seller,name="index_seller"),
    path('register_seller/',views.register_seller,name="register_seller"),
    path('otp_seller/',views.otp_seller, name="otp_seller"),
    path('login_seller/',views.login_seller, name="login_seller"),
    path('logout_seller/',views.logout_seller, name="logout_seller"),
    path('add_to_cart/<int:pk>',views.add_to_cart, name="add_to_cart"),
    path('basket',views.basket, name="basket"),
    path('remove_cart/<int:pk>',views.remove_cart, name="remove_cart"),
    path('checkout/',views.checkout, name="checkout"),
]
