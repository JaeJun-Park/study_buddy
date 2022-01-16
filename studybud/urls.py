
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls), # not yet learn
    path('', include('base.urls')),
]
