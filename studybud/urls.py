
from django.contrib import admin
from django.urls import path, include


urlpatterns = [ 
    path('admin/', admin.site.urls), # not yet learn
    path('', include('base.urls')),  # core urls routing만 project의 urls.py가 담당하고 나머지는 app의 urls.py로 위임
]
