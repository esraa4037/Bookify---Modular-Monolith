from modules.events.event_dispatcher import EventDispatcher
from modules.events.events import AppointmentBookedEvent
from .notification_service import NotificationService
from .confirmation_handlers import PatientConfirmationHandler, DoctorConfirmationHandler


def initialize_confirmation_module():
    """
    Initialize the Confirmation Module and subscribe patient and doctor handlers to the event.
    """
    event_dispatcher = EventDispatcher()
    notification_service = NotificationService()

    # Initialize handlers
    patient_handler = PatientConfirmationHandler(notification_service)
    doctor_handler = DoctorConfirmationHandler(notification_service)

    # Subscribe handlers to the event
    event_dispatcher.subscribe(AppointmentBookedEvent.EVENT_NAME, patient_handler.handle_appointment_booked)
    event_dispatcher.subscribe(AppointmentBookedEvent.EVENT_NAME, doctor_handler.handle_appointment_booked)
