from django.contrib import admin
from .models import Restaurant, Doctor

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'rating')
    search_fields = ('name', 'cuisine')
    list_filter = ('cuisine',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience')
    search_fields = ('name', 'specialization')
    list_filter = ('specialization',)