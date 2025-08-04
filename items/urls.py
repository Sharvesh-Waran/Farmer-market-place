from django.urls import path

from . import views

app_name = 'items'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.browse, name='browse'),
    path('<int:pk>/', views.detail, name='detail'),
]