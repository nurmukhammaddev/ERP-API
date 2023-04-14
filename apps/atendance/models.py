from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.common.models import BaseModel
from apps.staf.models import Staff

from .choises import STATUS


class Attendance(BaseModel):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS)
    date = models.DateField()
    time = models.TimeField()
    delta_time = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
        db_table = "attendance"
        ordering = ["-created_at"]

    def __str__(self):
        return self.staff.name
