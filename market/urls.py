from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

from core.views import index, contact

urlpatterns = [
    path("", include('core.urls')),
    path('items/', include('items.urls')),
    path("admin/", admin.site.urls),
    path('dashboard', include('dashboard.urls')),
] 
