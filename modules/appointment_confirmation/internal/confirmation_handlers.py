from .notification_service import NotificationService

# Constatnts
DOCTOR_NAME = "Mohamed Ahmed"


class PatientConfirmationHandler:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def handle_appointment_booked(self, event):
        """
        Handle the AppointmentBookedEvent for the patient.
        """
        confirmation_message = (
            f"*** Appointment confirmed ***\n"
            f"=============================\n"
            f"Doctor name: {DOCTOR_NAME}\n"
            f"Patient name: {event.patient_name}\n"
            f"Booked at: {event.booked_at}\n"
        )
        self.notification_service.send_notification(event.patient_name, confirmation_message)


class DoctorConfirmationHandler:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def handle_appointment_booked(self, event):
        """
        Handle the AppointmentBookedEvent for the doctor.
        """
        confirmation_message = (
            f"*** Appointment confirmed ***\n"
            f"=============================\n"
            f"Doctor name: {DOCTOR_NAME}\n"
            f"Patient name: {event.patient_name}\n"
            f"Booked at: {event.booked_at}\n"
        )
        self.notification_service.send_notification(DOCTOR_NAME, confirmation_message)
