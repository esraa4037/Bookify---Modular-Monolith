from common.repositories.slot import SlotRepositoryInterface
from common.exceptions.exceptions import SlotPastTimeError
from common.domain.slot import Slot
from .models import Slot as SlotModel
from datetime import datetime


class SlotRepository(SlotRepositoryInterface):
    def add_slot(self, slot_data) -> Slot:
        """Create new slot."""
        
        time_string = slot_data.get('time')
        # Parse the datetime string
        time = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        if time < datetime.now():
            raise SlotPastTimeError
        # Save the appointment in the database
        db_slot = SlotModel.objects.create(**slot_data)
        return Slot(
            id=db_slot.id,
            time=db_slot.time,
            is_reserved=db_slot.is_reserved,
            cost=db_slot.cost,
        )

    def reserve_slot(self, slot_id) -> Slot:
        """ Reserve an existing slot

        Args:
            slot_id (UUID): primary key

        Returns:
            Slot (In case of success): domain model
            or
            None (In case of failure)
        """
        updated_count = SlotModel.objects.filter(id=slot_id).update(is_reserved=True)
        if updated_count:
            db_slot = SlotModel.objects.get(id=slot_id)
            return Slot(
                id=db_slot.id,
                time=db_slot.time,
                is_reserved=db_slot.is_reserved,
                cost=db_slot.cost,
            )
        else:
            return None

    def get_all_slots(self) -> list[int]:
        slots = SlotModel.objects.all()
        return [
            Slot(
                id=slot.id,
                time=slot.time,
                is_reserved=slot.is_reserved,
                cost=slot.cost,
            )
            for slot in slots
        ]

    def get_available_slots(self) -> list[int]:
        slots = SlotModel.objects.filter(time__gt=datetime.now(), is_reserved=False)
        return [
            Slot(
                id=slot.id,
                time=slot.time,
                is_reserved=slot.is_reserved,
                cost=slot.cost,
            )
            for slot in slots
        ]

    def get_upcoming_reserved_slots_ids(self) -> list[int]:
        """Get all upcoming appointments."""
        slots_ids = SlotModel.objects.filter(time__gt=datetime.now(), is_reserved=True).values_list('id', flat=True)
        return slots_ids
