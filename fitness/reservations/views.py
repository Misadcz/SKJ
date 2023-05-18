from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import User,Instructor,Workout,Gym,Reservation,Equipment
from .forms import ReservationForm,WorkoutForm,GymForm,UserForm,InstructorForm
# Create your views here.

def addnewgym(request):
    g_form = GymForm(request.POST)
    if g_form.is_valid():
        name = g_form.cleaned_data['name']
        town = g_form.cleaned_data['town']
        description = g_form.cleaned_data['description']
        entry = g_form.cleaned_data['entry']
        gym = Gym(
            name=name,
            town=town,
            description=description,
            entry=entry,
        )
        gym.save()
        return redirect('index')
    
def instructor_detail_main(request,gym_id,instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/instructor_detail_main.html', {'instructor': instructor,'gym' : gym})
    
    
def instructor_detail_main_2(request,gym_id,instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/instructor_detail_main_2.html', {'instructor': instructor,'gym' : gym})
 
    
    
def user_detail_main(request,gym_id,user_id):
    user = get_object_or_404(User, pk=user_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/user_detail_main.html', {'user': user,'gym' : gym})

def workout_detail_main(request,gym_id,workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/workout_detail_main.html', {'workout': workout,'gym' : gym})

def index(request):
    gyms = Gym.objects.all()
    return render(request,'reservations/index.html',{'gyms':gyms})

def gym_add(request):
    gym_form = GymForm(request.POST)
    return render(request, 'reservations/gym_add.html', {'gym_form' : gym_form})


def gym(request,gym_id):
    instructors = Instructor.objects.all()
    workouts = Workout.objects.all()
    users = User.objects.all()
    gym = get_object_or_404(Gym,pk = gym_id)
    reservations =  Reservation.objects.filter(gym = gym)
    reservation_form = ReservationForm()
    return render(request,'reservations/gym.html',{'instructors' : instructors ,'users' : users,'workouts' : workouts,'gym' : gym, 'reservations' : reservations,'reservation_form' : reservation_form})

def user_add(request,gym_id):
    gym = get_object_or_404(Gym,pk = gym_id)
    user_form = UserForm(request.POST)
    return render(request, 'reservations/user_add.html', {'user_form' : user_form, 'gym' : gym})
    

def adduser(request,gym_id):
    gym = get_object_or_404(Gym,pk = gym_id)
    u_form = UserForm(request.POST)
    if u_form.is_valid():
        firstname = u_form.cleaned_data['firstname']
        lastname = u_form.cleaned_data['lastname']
        email = u_form.cleaned_data['email']
        age = u_form.cleaned_data['age']
        password = u_form.cleaned_data['password']
        user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            age=age,
            password=password,
        )
        user.save()
        return redirect('gym', gym_id=gym.id)
    
    
    
def instructor_add(request,gym_id):
    gym = get_object_or_404(Gym,pk = gym_id)
    instructor_form = InstructorForm(request.POST)
    return render(request, 'reservations/instructor_add.html', {'instructor_form' : instructor_form, 'gym' : gym})
    

def addinstructor(request,gym_id):
    gym = get_object_or_404(Gym,pk = gym_id)
    i_form = InstructorForm(request.POST)
    if i_form.is_valid():
        firstname = i_form.cleaned_data['firstname']
        lastname = i_form.cleaned_data['lastname']
        email = i_form.cleaned_data['email']
        phone_number = i_form.cleaned_data['phone_number']
        instructor = Instructor(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
        )
        instructor.save()
        return redirect('gym', gym_id=gym.id)
    
    
    
def workout_add(request,gym_id):
    gym = get_object_or_404(Gym,pk = gym_id)
    workout_form = WorkoutForm(request.POST)
    return render(request, 'reservations/workout_add.html', {'workout_form' : workout_form, 'gym' : gym})
    

def addworkout(request,gym_id):
    gym = get_object_or_404(Gym,pk = gym_id)
    w_form = WorkoutForm(request.POST)
    if w_form.is_valid():
        name = w_form.cleaned_data['name']
        description = w_form.cleaned_data['description']
        duration = w_form.cleaned_data['duration']
        difficulty = w_form.cleaned_data['difficulty']
        instructor = w_form.cleaned_data['instructor']
        equipment = w_form.cleaned_data['equipment']
        workout = Workout(
            name=name,
            description=description,
            duration=duration,
            difficulty=difficulty,
            instructor=instructor,
            equipment=equipment,
        )
        workout.save()
        return redirect('gym', gym_id=gym.id)
    
    
    
    
def reservation_add(request, gym_id):
    gym = get_object_or_404(Gym,pk = gym_id)
    reservation_form = ReservationForm()
    return render(request, 'reservations/reservation_add.html', {'gym' : gym,'reservation_form' : reservation_form})



def addreservation(request,gym_id):
    gym = get_object_or_404(Gym,pk = gym_id)
    r_form = ReservationForm(request.POST)
    if r_form.is_valid():
        reservation_date = r_form.cleaned_data['reservation_date']
        user = r_form.cleaned_data['user']
        workout = r_form.cleaned_data['workout']
        reservation = Reservation(
            reservation_date=reservation_date,
            gym=gym,
            user=user,
            workout=workout,
        )
        reservation.save()
        return redirect('gym', gym_id=gym.id)
    
def reservation_detail(request, gym_id, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation,'gym' : gym})

def user_detail(request,gym_id, reservation_id, user_id):
    user = get_object_or_404(User, pk=user_id)
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/user_detail.html', {'user': user,'reservation': reservation,'gym' : gym})


def instructor_detail(request,gym_id, reservation_id,workout_id, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    workout = get_object_or_404(Workout, pk=workout_id)
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/instructor_detail.html', {'workout' : workout ,'instructor': instructor,'reservation': reservation,'gym' : gym})


def workout_detail(request,gym_id, reservation_id, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/workout_detail.html', {'workout': workout,'reservation': reservation,'gym' : gym})

def equipment_detail(request,gym_id, reservation_id, workout_id,equipment_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    workout = get_object_or_404(Workout, pk=workout_id)
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/equipment_detail.html', {'workout': workout,'reservation': reservation,'gym' : gym, 'equipment' : equipment})

def equipment_detail_main(request,gym_id, workout_id,equipment_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    workout = get_object_or_404(Workout, pk=workout_id)
    gym = get_object_or_404(Gym,pk = gym_id)
    return render(request, 'reservations/equipment_detail_main.html', {'workout': workout,'gym' : gym, 'equipment' : equipment})



