from abc import ABC, abstractmethod
from common.domain.appointment import Appointment

class AppointmentRepositoryInterface(ABC):
    @abstractmethod
    def book_appointment(self, slot_id: int, patient_id: int) -> Appointment:
        """Book an appointment for a patient."""
        pass

    @abstractmethod
    def cancel_appointment(self, appointment_id: int) -> None:
        """Cancel an appointment."""
        pass

    @abstractmethod
    def complete_appointment(self, appointment_id: int) -> Appointment:
        """Mark an appointment as completed."""
        pass

    @abstractmethod
    def get_upcoming_appointments(self) -> list[Appointment]:
        """Get all upcoming appointments."""
        pass
