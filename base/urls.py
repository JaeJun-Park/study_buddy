from django.urls import path
from . import views # for each urls, connect view page

urlpatterns = [ 
    path('', views.home, name="home"), # reference a view (specific url) by its name
    path('room/', views.room, name="room"), 
]


