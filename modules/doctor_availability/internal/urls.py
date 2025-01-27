from django.urls import path
from .views import list_all_slots, list_available_slots, add_slot

urlpatterns = [
    path('slots/all/', list_all_slots, name='list_all_slots'),
    path('slots/available/', list_available_slots, name='list_available_slots'),
    path('slots/add/', add_slot, name='add_slot'),
]
