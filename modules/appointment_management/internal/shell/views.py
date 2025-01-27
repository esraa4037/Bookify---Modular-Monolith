import json
# Rest frame work
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Swagger
from drf_yasg.utils import swagger_auto_schema
# Services
from modules.appointment_management.internal.factories import get_doctor_appointment_management_service
# Exceptions
from common.exceptions.exceptions import InvalidAppointmentActionError
# Docs
from .docs import (
    cancel_appointment_responses,
    cancel_appointment_manual_parameters,
    complete_appointment_manual_parameters,
    complete_appointment_responses,
    upcoming_appointments_responses,
)

# Initialize the service using the factory
service = get_doctor_appointment_management_service()


@swagger_auto_schema(
    method='post',
    operation_description="Cancel an appointment by its ID.",
    responses=cancel_appointment_responses,
    manual_parameters=cancel_appointment_manual_parameters,
)
@api_view(['POST'])
def cancel_appointment(request, appointment_id):
    """
    Cancel an appointment
    """
    try:
        appointmet = service.cancel_appointment(appointment_id)
        return Response(
            {"message": "Appointment cancelled successfully."},
            status=status.HTTP_200_OK
        )
    except InvalidAppointmentActionError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method='post',
    operation_description="Mark an appointment as completed",
    manual_parameters=complete_appointment_manual_parameters,
    responses=complete_appointment_responses
)
@api_view(['POST'])
def complete_appointment(request, appointment_id):
    """Mark an appointment as completed"""
    try:
        appointmet = service.complete_appointment(appointment_id)
        return Response(
            {"message": "Appointment marked as completed."},
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method='get',
    operation_description="Get all upcoming appointments.",
    responses=upcoming_appointments_responses
)
@api_view(['GET'])
def get_upcoming_appointments(request):
    """
    Get all upcoming appointments.
    """
    try:
        appointments = service.get_upcoming_appointments()
        serialized_appointments = [appointment.to_dict() for appointment in appointments]
        return Response(
            {"appointments": serialized_appointments},
            status=status.HTTP_200_OK
        )
    except Exception as e:
        # Handle unexpected errors
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )