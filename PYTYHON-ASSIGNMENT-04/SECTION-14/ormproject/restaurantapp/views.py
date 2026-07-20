from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product


def product_list(request):

    products = Product.objects.filter(
        Q(category__name="Electronics") |
        Q(price__lt=1000)
    )

    paginator = Paginator(products, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "product_list.html", {
        "page_obj": page_obj
    })