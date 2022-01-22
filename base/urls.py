from django.urls import path
from . import views # for each urls, connect view page

urlpatterns = [ # 사용자로 부터 http요청이 들어오면 이 배열 내부에서 패턴을 찾아 연결시킨다
    path('', views.home, name="home"), 
    #2번째 아규먼트 : request 오브젝트 받아서 페이지 렌더링하는 함수 주소전달
    #3번째 아규먼트 : 이 url을 대표하는 이름값을 설정, 템플릿에서 a태그 등으로 경로를 쉽게 연결해주기 위해서 이런 name설정이 필요하다.
    path('room/<str:pk>/', views.room, name="room"), 
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
]


