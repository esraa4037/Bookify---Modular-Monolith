from django.urls import path
from .views import book_appointment


urlpatterns = [
    path('appointment/book/', book_appointment, name='book_appointment'),
]
