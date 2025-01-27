from common.repositories.appointment import AppointmentRepositoryInterface
from apps.slot.repositories import SlotRepository
from common.exceptions.exceptions import SlotNotReservedError
from common.domain.appointment import Appointment
from .models import Appointment as AppointmentModel
from modules.doctor_availability.shared.facade import DoctorAvailabilityFacade


class AppointmentRepository(AppointmentRepositoryInterface):
    def book_appointment(self, slot_id, patient_id) -> Appointment:
        """Book an appointment for patient at a specific time slot."""
        # Save the appointment in the database
        db_appointment = AppointmentModel.objects.create(
            slot_id=slot_id,
            patient_id=patient_id,
            status=AppointmentModel.UPCOMING_STATUS,
        )
        
        # Reserve the slot
        doctor_availability = DoctorAvailabilityFacade()
        slot = doctor_availability.reserve_slot(slot_id)
        if slot:
            return Appointment(
                id=db_appointment.id,
                slot_id=db_appointment.slot_id,
                patient_id=db_appointment.patient_id,
                patient_name=db_appointment.patient.name,
                reserved_at=db_appointment.reserved_at,
                status=db_appointment.status,
            )
        else:
            raise SlotNotReservedError("Slot can't be reserved.")

    def cancel_appointment(self, appointment_id) -> None:
        """Cancel an appointment by updating its status to canceled."""
        appointment = AppointmentModel.objects.filter(id=appointment_id).update(status=AppointmentModel.CANCELED_STATUS)

    def complete_appointment(self, appointment_id) -> Appointment:
        """Mark an appointment as completed by updating its status to compoleted."""
        appointment = AppointmentModel.objects.filter(id=appointment_id).update(status=AppointmentModel.COMPLETED_STATUS)

    def get_upcoming_appointments(self) -> list[Appointment]:
        """Get all upcoming appointments."""
        slot_repository = SlotRepository()
        upcoming_reserved_slots_ids = slot_repository.get_upcoming_reserved_slots_ids()
        db_appointments = AppointmentModel.objects.filter(
                                slot_id__in=upcoming_reserved_slots_ids,
                                status=AppointmentModel.UPCOMING_STATUS
                            )
        return [
            Appointment(
                id=db_appointment.id,
                slot_id=db_appointment.slot_id,
                patient_id=db_appointment.patient_id,
                patient_name=db_appointment.patient.name,
                reserved_at=db_appointment.reserved_at,
                status=db_appointment.status,
            )
            for db_appointment in db_appointments
        ]
