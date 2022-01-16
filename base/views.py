from django.shortcuts import render
 
# to create a view, we should make function like this
def home(request): # http object
    return render(request, 'home.html')
    
def room(request): 
    return render(request, 'room.html')