from django.urls import path
from . import views # for each urls, connect view page

urlpatterns = [ # 사용자로 부터 http요청이 들어오면 이 배열 내부에서 패턴을 찾아 연결시킨다
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"), 
    path('room/<str:pk>/', views.room, name="room"), 
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-messgae/<str:pk>/', views.deleteMessage, name="delete-message"),
]



