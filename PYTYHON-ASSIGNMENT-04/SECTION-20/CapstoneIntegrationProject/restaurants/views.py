from django.shortcuts import render
from django.db.models import Q
from .models import Restaurant

def check_and_seed_data():
    if Restaurant.objects.count() == 0:
        seed_data = [
            {"name": "Trattoria Bella", "cuisine": "Italian", "location": "New York"},
            {"name": "Taj Mahal Palace", "cuisine": "Indian", "location": "Mumbai"},
            {"name": "Sushi Saito", "cuisine": "Japanese", "location": "Tokyo"},
            {"name": "La Taqueria", "cuisine": "Mexican", "location": "San Francisco"},
            {"name": "Le Bistrot Parisian", "cuisine": "French", "location": "Paris"},
            {"name": "Golden Dragon", "cuisine": "Chinese", "location": "New York"},
            {"name": "Peshawri", "cuisine": "Indian", "location": "Mumbai"},
            {"name": "Bella Italia", "cuisine": "Italian", "location": "London"},
            {"name": "Burger Craft & Co.", "cuisine": "American", "location": "London"},
            {"name": "Sakura Zen", "cuisine": "Japanese", "location": "San Francisco"},
            {"name": "Amigo Mexican Grill", "cuisine": "Mexican", "location": "Chicago"},
            {"name": "Olive & Oregano", "cuisine": "Mediterranean", "location": "Chicago"},
        ]
        for item in seed_data:
            Restaurant.objects.create(**item)

def search_restaurant(request):
    check_and_seed_data()
    
    query = request.GET.get("q", "").strip()
    cuisine_filter = request.GET.get("cuisine", "").strip()
    location_filter = request.GET.get("location", "").strip()

    restaurants = Restaurant.objects.all()

    if query:
        restaurants = restaurants.filter(
            Q(name__icontains=query) |
            Q(cuisine__icontains=query) |
            Q(location__icontains=query)
        )
    
    if cuisine_filter:
        restaurants = restaurants.filter(cuisine__iexact=cuisine_filter)
        
    if location_filter:
        restaurants = restaurants.filter(location__iexact=location_filter)

    # Extract distinct values for UI filters
    all_cuisines = Restaurant.objects.values_list('cuisine', flat=True).distinct()
    all_locations = Restaurant.objects.values_list('location', flat=True).distinct()

    return render(
        request,
        "restaurant_search.html",
        {
            "restaurants": restaurants,
            "query": query,
            "selected_cuisine": cuisine_filter,
            "selected_location": location_filter,
            "all_cuisines": all_cuisines,
            "all_locations": all_locations,
        }
    )