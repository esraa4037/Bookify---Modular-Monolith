import json
from functools import wraps
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from common.exceptions.exceptions import SlotNotAvailableError, AppointmentNotBookedError
from .factories import get_appointment_booking_use_cases
from .docs import book_appointment_request, book_appointment_responses

def inject_appointment_use_cases(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        # Inject the use cases into the view's kwargs
        kwargs['appointment_use_cases'] = get_appointment_booking_use_cases()
        return view_func(*args, **kwargs)
    return wrapped_view

@swagger_auto_schema(
    method='post',
    operation_description='Book a new appointment.',
    request_body=book_appointment_request,
    responses=book_appointment_responses,
)
@api_view(['POST'])
@inject_appointment_use_cases
def book_appointment(request, appointment_use_cases):
    """
    Book a new appointment.
    """
    try:
        # Parse the request data
        data = json.loads(request.body)

        # Call the use case to book the appointment
        appointment = appointment_use_cases.book_appointment(
            slot_id=data['slot_id'],
            patient_id=data['patient_id'],
        )

        # Return the appointment details
        return Response({
            'id': appointment.id,
            'slot_id': appointment.slot_id,
            'patient_id': appointment.patient_id,
            'patient_name': appointment.patient_name,
            'reserved_at': appointment.reserved_at,
            'status': appointment.status
        }, status=status.HTTP_201_CREATED)

    except SlotNotAvailableError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    except AppointmentNotBookedError as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({'error': f'An unexpected error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
