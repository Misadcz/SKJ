from django.apps import AppConfig


class ReservationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservations'
    
class WorkoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workout'
    
class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
