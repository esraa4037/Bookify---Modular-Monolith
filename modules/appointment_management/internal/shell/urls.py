from django.urls import path
from .views import complete_appointment, cancel_appointment, get_upcoming_appointments


urlpatterns = [
    path('appointment/<uuid:appointment_id>/complete/', complete_appointment, name='complete_appointment'),
    path('appointment/<uuid:appointment_id>/cancel/', cancel_appointment, name='cancel_appointment'),
    path('appointment/upcoming-appointments/', get_upcoming_appointments, name='get_upcoming_appointments'),
]
