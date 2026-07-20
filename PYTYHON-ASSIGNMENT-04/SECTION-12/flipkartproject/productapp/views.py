from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


# Read
def product_list(request):

    products = Product.objects.all()

    return render(request, 'product_list.html',
                  {'products': products})


# Create
def add_product(request):

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:

        form = ProductForm()

    return render(request, 'product_form.html',
                  {'form': form})


# Update
def edit_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":

        form = ProductForm(request.POST,
                           instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:

        form = ProductForm(instance=product)

    return render(request,
                  'product_form.html',
                  {'form': form})


# Delete
def delete_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":

        product.delete()

        return redirect('product_list')

    return render(request,
                  'product_delete.html',
                  {'product': product})