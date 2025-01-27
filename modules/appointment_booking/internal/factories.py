from apps.appointment.repositories import AppointmentRepository
from modules.doctor_availability.shared.facade import DoctorAvailabilityFacade
from modules.events.event_dispatcher import EventDispatcher
from .use_cases import AppointmentBookingUseCases


def get_appointment_booking_use_cases():
    """
    Factory function to create and return the AppointmentBookingUseCases.
    """
    # Initialize dependencies
    appointment_repository = AppointmentRepository()
    doctor_availability_facade = DoctorAvailabilityFacade()
    event_dispatcher = EventDispatcher()  # Singleton instance

    # Inject the repository and facade into the use case
    return AppointmentBookingUseCases(appointment_repository, doctor_availability_facade, event_dispatcher)
