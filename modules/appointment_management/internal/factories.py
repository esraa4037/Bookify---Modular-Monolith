from apps.appointment.repositories import AppointmentRepository
from modules.appointment_management.internal.core.services import DoctorAppointmentManagementService

def get_doctor_appointment_management_service():
    """Factory function to create and return the DoctorAppointmentManagementService."""
    appointment_repository = AppointmentRepository()  # Create the repository
    return DoctorAppointmentManagementService(appointment_repository)  # Inject the repository into the service
