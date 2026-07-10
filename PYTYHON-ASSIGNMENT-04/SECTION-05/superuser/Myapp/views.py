from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("Welcome to Django Admin Customization Project")

def restaurant_list(request):
    return render(request, 'restaurant.html')

def doctor_list(request):
    return render(request, 'doctor.html')