from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to My Django Project!")

def explore(request):
    return HttpResponse("Explore the features of My Django Project!")