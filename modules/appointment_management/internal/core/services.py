from .entities import Appointment
from common.exceptions.exceptions import InvalidAppointmentActionError

class DoctorAppointmentManagementService:
    def __init__(self, appointment_repository):
        self.appointment_repository = appointment_repository

    def _mark_appointment_as_canceled(self, appointment_id):
        return self.appointment_repository.cancel_appointment(appointment_id)
    
    
    def _is_upcoming(self, appointment_id):
        upcoming_appointments = self.get_upcoming_appointments()
        if not any(str(upcoming.id) == str(appointment_id) for upcoming in upcoming_appointments):
            return False
        return True

    def cancel_appointment(self, appointment_id):
        """Cancel an appointment."""
        # check if the appointment is is upcoming
        is_upcoming = self._is_upcoming(appointment_id)
        if is_upcoming:
            return self._mark_appointment_as_canceled(appointment_id)
        else:
            raise InvalidAppointmentActionError('Past appointment can\'t be canceled')

    def complete_appointment(self, appointment_id):
        """Mark an appointment as completed."""
        return self.appointment_repository.complete_appointment(appointment_id)
        
    def get_upcoming_appointments(self):
        """List all upcoming appointments."""
        return self.appointment_repository.get_upcoming_appointments()

