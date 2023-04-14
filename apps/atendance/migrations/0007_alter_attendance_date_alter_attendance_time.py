# Generated by Django 4.2 on 2023-04-14 19:43

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("atendance", "0006_remove_attendance_delta_time_attendance_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 4, 14, 19, 43, 8, 948592, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="attendance",
            name="time",
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
