class Appointment:
    def __init__(self, slot_id, patient_id, reserved_at, status, id=None, patient_name=None):
        self.id = id
        self.slot_id = slot_id
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.reserved_at = reserved_at
        self.status = status
