from django.urls import path
from . import views # for each urls, connect view page

urlpatterns = [ 
    path('', views.home, name="home"), 
    #2번째 아규먼트 request 오브젝트 받아서 페이지 렌더링하는 함수 주소전달
    #3번째 아규먼트 reference a view (specific url) by its name
    path('room/<str:pk>/', views.room, name="room"), 
]


