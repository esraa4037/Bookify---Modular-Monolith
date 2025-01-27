import uuid
from django.db import models


class Slot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateTimeField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    is_reserved = models.BooleanField(default=False)

    class Meta:
        db_table = 'slot'
