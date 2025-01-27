import json
# Rest frame work
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Swagger
from drf_yasg.utils import swagger_auto_schema
# Services
from .services import get_doctor_availability_service
# Exceptions
from common.exceptions.exceptions import SlotPastTimeError
# Docs
from .docs import (
    add_slot_request,
    add_slot_responses,
    list_all_slots_responses,
    list_available_slots_responses,
)


# Initialize the service using the factory
service = get_doctor_availability_service()

@swagger_auto_schema(
    method='post',
    request_body=add_slot_request,
    responses=add_slot_responses,
)
@api_view(['POST'])
def add_slot(request):
    """
    Add a new time slot.
    """
    data = json.loads(request.body)
    try:
        slot = service.add_slot(data)
        return Response({
            'id': slot.id,
            'time': slot.time,
            'is_reserved': slot.is_reserved,
            'cost': float(slot.cost)
        }, status=status.HTTP_201_CREATED)
    except SlotPastTimeError:
        return Response({'error': SlotPastTimeError.MESSAGE}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses=list_all_slots_responses,
)
@api_view(['GET'])
def list_all_slots(request):
    """
    List all time slots (both available and reserved).
    """
    slots = service.get_all_slots()
    slots_data = [{
        'id': slot.id,
        'time': slot.time,
        'is_reserved': slot.is_reserved,
        'cost': float(slot.cost)
    } for slot in slots]
    
    return Response(slots_data)

@swagger_auto_schema(
    method='get',
    responses=list_available_slots_responses,
)
@api_view(['GET'])
def list_available_slots(request):
    """
    List all available time slots.
    """
    slots = service.get_available_slots()
    slots_data = [{
        'id': slot.id,
        'time': slot.time,
        'is_reserved': slot.is_reserved,
        'cost': float(slot.cost)
    } for slot in slots]
    
    return Response(slots_data)

