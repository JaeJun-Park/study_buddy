from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id': 1, 'name':'Lets learn python!'},
#     {'id': 2, 'name':'Design with me'},
#     {'id': 3, 'name':'Frontend developers'},
# ] 

# to create a view, we should make function like this
def home(request): # http object
    rooms = Room.objects.all()
    print(rooms)
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context) # request받아서 'home.html' 템플릿 렌더링해주는 django.shortcuts모듈 속 함수
    
def room(request, pk): 
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
    