from .entities import Appointment
from common.exceptions.exceptions import SlotNotAvailableError, AppointmentNotBookedError
from modules.events.events import AppointmentBookedEvent


class AppointmentBookingUseCases:
    def __init__(self, appointment_repository, doctor_availability_facade, event_dispatcher):
        """
        Initialize the use case with a repository and a facade for doctor availability.
        """
        self.appointment_repository = appointment_repository
        self.doctor_availability_facade = doctor_availability_facade
        self.event_dispatcher = event_dispatcher

    def _get_available_slots(self):
        """
        Get all available slots from the Doctor Availability module.
        """
        return self.doctor_availability_facade.list_available_slots()

    def book_appointment(self, slot_id, patient_id):
        """
        Book an appointment if the slot is available.
        Raises:
            SlotNotAvailableError: If the slot is not available.
            AppointmentNotBookedError: If the appointment could not be booked.
        """
        # Check if the slot is available
        available_slots = self._get_available_slots()

        if not any(str(slot.id) == str(slot_id) for slot in available_slots):
            raise SlotNotAvailableError("The requested slot is not available.")

        # Book the appointment using the repository
        saved_appointment = self.appointment_repository.book_appointment(slot_id, patient_id)
        if not saved_appointment:
            raise AppointmentNotBookedError("The appointment could not be booked.")

        # Publish an event for appointment confirmation
        appointment_booked_event = AppointmentBookedEvent(
            appointment_id=saved_appointment.id,
            patient_id=saved_appointment.patient_id,
            patient_name=saved_appointment.patient_name,
            slot_id=saved_appointment.slot_id,
            booked_at=saved_appointment.reserved_at
        )
        self.event_dispatcher.publish(AppointmentBookedEvent.EVENT_NAME, appointment_booked_event)

        return saved_appointment
