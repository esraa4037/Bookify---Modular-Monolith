import uuid
from django.db import models
from apps.slot.models import Slot
from apps.patient.models import Patient

# Create your models here.
class Appointment(models.Model):
    COMPLETED_STATUS = ("completed", "Completed")
    CANCELED_STATUS = ("canceled", "Canceled")
    UPCOMING_STATUS = ("upcoming", "Upcoming")
    STATUS_CHOICES = [COMPLETED_STATUS, CANCELED_STATUS, UPCOMING_STATUS]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slot = models.OneToOneField(Slot, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    reserved_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default=UPCOMING_STATUS, choices=STATUS_CHOICES, max_length=10)

    class Meta:
        db_table = 'appointment'
