from django.db import models

# Create your models here.

class Room(models.Model): # models.Model을 상속받음
    #host = 
    #topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) # only when it created 

    def __str__(self):
        return self.name
