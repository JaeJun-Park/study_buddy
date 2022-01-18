
from django.contrib import admin
from django.urls import path, include


urlpatterns = [ # 사용자로 부터 http요청이 들어오면 이 배열 내부에서 패턴을 찾아 연결시킨다
    path('admin/', admin.site.urls), # not yet learn
    path('', include('base.urls')),  # core urls routing만 project의 urls.py가 담당하고 나머지는 app의 urls.py로 위임
]
