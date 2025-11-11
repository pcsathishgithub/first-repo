from django.contrib import admin 
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path 
from . import views
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('booking/items/', views.BookingView.as_view(), name='booking-items'),
    path('booking/items/<int:pk>/', views.SingleBookingItemView.as_view(), name='single-booking-item'),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),
    
]