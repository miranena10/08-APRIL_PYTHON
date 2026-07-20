from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("otp/", views.send_otp, name="otp"),
    path("verify/", views.verify_otp, name="verify"),
]