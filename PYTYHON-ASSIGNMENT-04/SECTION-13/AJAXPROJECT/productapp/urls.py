from django.urls import path
from . import views

urlpatterns = [
    # Display all products
    path('', views.product_list, name='product_list'),

    # Add new product
    path('add/', views.add_product, name='add_product'),

    # Edit product
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),

    # AJAX Delete product
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]