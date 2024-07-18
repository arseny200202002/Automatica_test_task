from django.contrib import admin
from django.urls import path, include

from .spectacular import urlpatterns as spec_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
] + spec_urls
