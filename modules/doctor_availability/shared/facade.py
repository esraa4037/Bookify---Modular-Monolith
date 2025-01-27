from modules.doctor_availability.internal.services import get_doctor_availability_service

class DoctorAvailabilityFacade:
    def __init__(self):
        # Initialize the service using the factory
        self.service = get_doctor_availability_service()

    def list_available_slots(self):
        """List all available slots."""
        return self.service.get_available_slots()

    def reserve_slot(self, slot_id):
        """Reserve a slot."""
        return self.service.reserve_slot(slot_id)
