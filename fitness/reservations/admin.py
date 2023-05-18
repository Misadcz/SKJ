from django.contrib import admin
from .models import Gym,User,Instructor,Workout,Reservation,Equipment
# Register your models here.

admin.site.register(Gym)
admin.site.register(User)
admin.site.register(Instructor)
admin.site.register(Workout)
admin.site.register(Reservation)
admin.site.register(Equipment)