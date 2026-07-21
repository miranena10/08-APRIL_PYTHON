from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pay/", views.pay, name="pay"),
    path("payment-callback/", views.payment_callback, name="payment_callback"),
    path("food/", views.food, name="food"),
    path("paypal/", views.paypal, name="paypal"),
]