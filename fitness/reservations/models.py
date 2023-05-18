from django.db import models

class Instructor(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname

class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Equipment(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    year_of_production = models.IntegerField()
    
    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    duration = models.IntegerField()
    difficulty = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Gym(models.Model):
    name = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    entry = models.IntegerField()
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.workout.name + ' - ' + self.user.firstname + " "+ self.user.lastname 


