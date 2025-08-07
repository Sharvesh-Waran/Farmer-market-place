from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('items/', views.getAllItems, name='get-all-items'),
    path('browse/', views.browse_transactions, name='browse-all-items'),
    path('new/', views.newItem, name='create-new-item'),
    path('items/<int:pk>/', views.getItem, name='get-item'),
    path('items/<int:pk>/buy/', views.buyItem, name='buy-item'),
]