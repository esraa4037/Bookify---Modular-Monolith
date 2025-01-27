class SlotNotAvailableError(Exception):
    """Raised when the requested slot is not available."""
    pass

class SlotNotReservedError(Exception):
    """Raised when the requested slot is not available."""
    pass

class SlotPastTimeError(Exception):
    """Raised when the requested slot is not available."""
    MESSAGE = "Time slot cannot be in the past."

class AppointmentNotBookedError(Exception):
    """Raised when the appointment could not be booked."""
    pass

class InvalidAppointmentActionError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"InvalidAppointmentAction: {self.message}"
