from django.shortcuts import render
from .forms import AddRestaurantForm

def add_restaurant(request):

    if request.method == "POST":
        form = AddRestaurantForm(request.POST)

        if form.is_valid():
            data = {
                "restaurant_name": form.cleaned_data["restaurant_name"],
                "cuisine_type": form.cleaned_data["cuisine_type"],
                "contact_email": form.cleaned_data["contact_email"],
            }

            return render(request, "restaurant_success.html", data)

    else:
        form = AddRestaurantForm()

    return render(request, "add_restaurant.html", {"form": form})