from django.shortcuts import render
from django.conf import settings

def map_page(request):
    api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')
    return render(request, 'maps.html', {
        'google_maps_api_key': api_key
    })
