class Appointment:
    def __init__(self, slot_id, patient_id, reserved_at, status, id=None, patient_name=None):
        self.id = id
        self.slot_id = slot_id
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.reserved_at = reserved_at
        self.status = status

    def to_dict(self):
        """Convert the Appointment object to a dictionary."""
        return {
            "id": self.id,
            "slot_id": self.slot_id,
            "patient_id": self.patient_id,
            "patient_name": self.patient_name,
            "reserved_at": self.reserved_at,
            "status": self.status,
        }