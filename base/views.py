from django.shortcuts import render
 
rooms = [
    {'id': 1, 'name':'Lets learn python!'},
    {'id': 2, 'name':'Design with me'},
    {'id': 3, 'name':'Frontend developers'},
] # the datas which we gonna render inside of our templates

# to create a view, we should make function like this
def home(request): # http object
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context) # request받아서 'home.html' 템플릿 렌더링해주는 django.shortcuts모듈 속 함수
    
def room(request, pk): 
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)