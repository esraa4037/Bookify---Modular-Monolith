from dataclasses import dataclass
from datetime import datetime

@dataclass
class AppointmentBookedEvent:
    appointment_id: str
    patient_id: str
    patient_name: str
    slot_id: str
    booked_at: datetime

    EVENT_NAME = "AppointmentBookedEvent"
