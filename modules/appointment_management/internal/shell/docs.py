from drf_yasg import openapi
from rest_framework import status


########################### Cancel appointment #############################
cancel_appointment_responses = {
    status.HTTP_200_OK: openapi.Response(
        description="Appointment cancelled successfully.",
        examples={
            "application/json": {
                "message": "Appointment cancelled successfully."
            }
        }
    ),
    status.HTTP_400_BAD_REQUEST: openapi.Response(
        description="Invalid appointment action.",
        examples={
            "application/json": {
                "error": "Invalid appointment action."
            }
        }
    ),
    status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
        description="Internal server error.",
        examples={
            "application/json": {
                "error": "An unexpected error occurred."
            }
        }
    ),
}

cancel_appointment_manual_parameters = [
    openapi.Parameter(
        name='appointment_id',
        in_=openapi.IN_PATH,
        type=openapi.TYPE_STRING,
        description="The ID of the appointment to cancel.",
        required=True
    ),
]


########################### Complete appointment #############################
complete_appointment_manual_parameters = [
    openapi.Parameter(
        name="appointment_id",
        in_=openapi.IN_PATH,
        type=openapi.TYPE_STRING,
        description="The ID of the appointment to mark as completed",
        required=True
    )
]

complete_appointment_responses={
    200: openapi.Response(
        description="Success response",
        examples={
            "application/json": {
                "message": "Appointment marked as completed."
            }
        }
    ),
    500: openapi.Response(
        description="Error response",
        examples={
            "application/json": {
                "error": "Error message here"
            }
        }
    )
}


########################### Upcoming appointments #############################
upcoming_appointments_responses = {
    status.HTTP_200_OK: openapi.Response(
        description="Upcoming appointments retrieved successfully.",
        examples={
            "application/json": {
                "appointments": [
                    {
                        "id": "123",
                        "patient_name": "John Doe",
                        "appointment_time": "2023-10-10T14:00:00Z"
                    },
                    {
                        "id": "456",
                        "patient_name": "Jane Smith",
                        "appointment_time": "2023-10-11T10:00:00Z"
                    }
                ]
            }
        }
    ),
    status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
        description="Internal server error.",
        examples={
            "application/json": {
                "error": "An unexpected error occurred."
            }
        }
    ),
}