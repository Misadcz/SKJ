"""
URL configuration for fitness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservations import views
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = 'index'),
    path('gym/<int:gym_id>',views.gym, name='gym'),
    path('gym/<int:gym_id>/addreservation',views.addreservation, name='addreservation'),
]
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = 'index'),
    path('add',views.gym_add, name='gym_add'),
    path('addnewgym',views.addnewgym, name='addnewgym'),
    path('gym/<int:gym_id>',views.gym, name='gym'),
    path('gym/<int:gym_id>/user/add',views.user_add, name='user_add'),
    path('gym/<int:gym_id>/user/adduser',views.adduser, name='adduser'),
    
    
    path('gym/<int:gym_id>/instructor/add',views.instructor_add, name='instructor_add'),
    path('gym/<int:gym_id>/instructor/addinstructor',views.addinstructor, name='addinstructor'),
    
    path('gym/<int:gym_id>/workout/add',views.workout_add, name='workout_add'),
    path('gym/<int:gym_id>/workout/adduser',views.addworkout, name='addworkout'),
    
    path('gym/<int:gym_id>/user/<int:user_id>',views.user_detail_main, name='user_detail_main'),
    path('gym/<int:gym_id>/instructor/<int:instructor_id>',views.instructor_detail_main, name='instructor_detail_main'),
    path('gym/<int:gym_id>/workout/<int:workout_id>/instructor/<int:instructor_id>',views.instructor_detail_main_2, name='instructor_detail_main_2'),
    
    
    path('gym/<int:gym_id>/workout/<int:workout_id>',views.workout_detail_main, name='workout_detail_main'),
    path('gym/<int:gym_id>/workout/<int:workout_id>/equipment/<int:equipment_id>',views.equipment_detail_main, name='equipment_detail_main'),
    
    path('gym/<int:gym_id>/addreservation',views.addreservation, name='addreservation'),
    path('gym/<int:gym_id>/add',views.reservation_add, name='reservation_add'),
    path('gym/<int:gym_id>/reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('gym/<int:gym_id>/reservation/<int:reservation_id>/user/<int:user_id>', views.user_detail, name='user_detail'),
    path('gym/<int:gym_id>/reservation/<int:reservation_id>/workout/<int:workout_id>', views.workout_detail, name='workout_detail'),
    path('gym/<int:gym_id>/reservation/<int:reservation_id>/workout/<int:workout_id>/instructor/<int:instructor_id>', views.instructor_detail, name='instructor_detail'),
    path('gym/<int:gym_id>/reservation/<int:reservation_id>/workout/<int:workout_id>/equipment/<int:equipment_id>', views.equipment_detail, name='equipment_detail'),
]
