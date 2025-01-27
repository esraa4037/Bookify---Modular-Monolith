from apps.slot.repositories import SlotRepository

class DoctorAvailabilityService:
    def __init__(self, slot_repository):
        self.slot_repository = slot_repository

    def get_all_slots(self):
        """List all slots."""
        return self.slot_repository.get_all_slots()

    def get_available_slots(self):
        """List only the available slots."""
        return self.slot_repository.get_available_slots()

    def add_slot(self, slot_data):
        """Add a new slot for the doctor."""
        return self.slot_repository.add_slot(slot_data)

    def reserve_slot(self, slot_id):
        """Reserve a slot."""
        return self.slot_repository.reserve_slot(slot_id)


def get_doctor_availability_service():
    """Factory function to create and return the DoctorAvailabilityService."""
    slot_repository = SlotRepository()  # Create the repository
    return DoctorAvailabilityService(slot_repository)  # Inject the repository into the service
