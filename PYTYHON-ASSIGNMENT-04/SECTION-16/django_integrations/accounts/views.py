import random

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .models import OTP


def home(request):
    return render(request, "accounts/home.html")


def send_otp(request):

    message = ""

    if request.method == "POST":

        email = request.POST["email"]

        otp = str(random.randint(100000, 999999))

        OTP.objects.create(
            email=email,
            otp=otp
        )

        send_mail(
            subject="Your OTP Code",
            message=f"Your OTP is {otp}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        message = "OTP sent successfully to your email."

    return render(request, "accounts/otp.html", {"message": message})


def verify_otp(request):

    if request.method == "POST":

        email = request.POST['email']
        otp = request.POST['otp']

        if OTP.objects.filter(email=email, otp=otp).exists():

            username = email.split("@")[0]

            return render(request,
                          "accounts/dashboard.html",
                          {
                              "username": username.capitalize(),
                              "email": email
                          })

        else:

            return render(request,
                          "accounts/otp.html",
                          {
                              "message": "Invalid OTP"
                          })

    return render(request, "accounts/otp.html")