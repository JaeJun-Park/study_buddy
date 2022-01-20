from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message
# we need to register this model with the admin panel "we wanna be able to view this item and work with it in the built-in admin panel"

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

