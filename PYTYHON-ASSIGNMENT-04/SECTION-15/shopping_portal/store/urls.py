from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('myorders/', views.my_orders, name='my_orders'),
    path('postproduct/', views.post_product, name='post_product'),
    path('reviews/', views.review_list, name='review_list'),

]

