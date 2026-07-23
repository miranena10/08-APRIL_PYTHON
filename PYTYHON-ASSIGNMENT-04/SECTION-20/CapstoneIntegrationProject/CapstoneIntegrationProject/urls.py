from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='landing'),
    path('admin/', admin.site.urls),

    # Task 1 - Restaurant Search
    path(
        'restaurants/',
        include('restaurants.urls')
    ),


    # Task 2 - Login + OTP
    path(
        'accounts/',
        include('accounts.urls')
    ),


    # Task 3 - Profile Management
    path(
        'profile/',
        include('profiles.urls')
    ),


    # Task 4 - Google Maps
    path(
        'maps/',
        include('mapsapp.urls')
    ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)