from django import forms
from .models import Gym,Instructor,Equipment,Reservation,User,Workout

class ReservationForm(forms.ModelForm):
    user = forms.HiddenInput()
    class Meta():
        model = Reservation
        exclude = ['gym']
        widgets = {
            'reservation_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
        
class WorkoutForm(forms.ModelForm):
    class Meta():
        model = Workout
        exclude = []
        
        
class UserForm(forms.ModelForm):
    class Meta():
        model = User
        exclude = []        
        
class GymForm(forms.ModelForm):
    class Meta():
        model = Gym
        exclude = []
        
class InstructorForm(forms.ModelForm):
    class Meta():
        model = Instructor
        exclude = []
        


