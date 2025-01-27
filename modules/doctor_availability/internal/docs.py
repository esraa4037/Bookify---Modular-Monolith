from rest_framework import status
from drf_yasg import openapi

add_slot_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['time', 'cost'],
    properties={
        'time': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        'cost': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
        'is_reserved': openapi.Schema(type=openapi.TYPE_BOOLEAN, default=False),
    },
)

add_slot_responses = {
    201: openapi.Response(
        description="Slot created successfully",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID),
                'time': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                'cost': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
                'is_reserved': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            },
        ),
    ),
}

list_all_slots_responses = {
    200: openapi.Response(
        description="List of all time slots",
        schema=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID),
                    'time': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                    'cost': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
                    'is_reserved': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                },
            ),
        ),
    ),
}

list_available_slots_responses = {
    200: openapi.Response(
        description="List of available time slots",
        schema=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID),
                    'time': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                    'cost': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
                    'is_reserved': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                },
            ),
        ),
    ),
}
