# docs.py
from drf_yasg import openapi

book_appointment_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['slot_id', 'patient_id'],
    properties={
        'slot_id': openapi.Schema(type=openapi.TYPE_STRING, description='The ID of the slot to book.'),
        'patient_id': openapi.Schema(type=openapi.TYPE_STRING, description='The ID of the patient booking the appointment.'),
    },
)

book_appointment_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_STRING, description='The ID of the booked appointment.'),
        'slot_id': openapi.Schema(type=openapi.TYPE_STRING, description='The ID of the booked slot.'),
        'patient_id': openapi.Schema(type=openapi.TYPE_STRING, description='The ID of the patient who booked the appointment.'),
        'patient_name': openapi.Schema(type=openapi.TYPE_STRING, description='The name of the patient.'),
        'reserved_at': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='The timestamp when the appointment was reserved.'),
        'status': openapi.Schema(type=openapi.TYPE_STRING, description='The status of the appointment.'),
    },
)

book_appointment_responses = {
    201: openapi.Response(description="Appointment booked successfully.", schema=book_appointment_response),
    400: openapi.Response(
        description="Bad Request",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message indicating the slot is not available.'),
            },
        ),
    ),
    500: openapi.Response(
        description="Internal Server Error",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message indicating the appointment could not be booked.'),
            },
        ),
    ),
}
