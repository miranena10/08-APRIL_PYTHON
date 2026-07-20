from django.shortcuts import render
from django.contrib.auth.decorators import *
from .models import *

@login_required(login_url='login')
def dashboard(request):

    if request.user.groups.filter(name='Seller').exists():
        return render(request, 'seller_dashboard.html')

    elif request.user.groups.filter(name='Buyer').exists():
        return render(request, 'buyer_dashboard.html')

    else:
        return render(request, 'home.html')
    
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def my_orders(request):
    return render(request, 'my_orders.html')

 

@permission_required('store.add_product', raise_exception=True)
def post_product(request):
    return render(request, 'post_product.html')

def review_list(request):
    reviews = Review.objects.all()

    return render(request, "review_list.html", {
        "reviews": reviews
    })