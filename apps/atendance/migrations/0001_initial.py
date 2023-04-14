# Generated by Django 4.2 on 2023-04-14 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("staf", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("kechqoldi", "Kechqoldi"),
                            ("vahtida kelgan", "Vahtida kelgan"),
                            ("kelmadi", "Kelmadi"),
                        ],
                        max_length=100,
                    ),
                ),
                ("delta_time", models.TimeField(default=0)),
                (
                    "staf",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="staf.staff"
                    ),
                ),
            ],
            options={
                "verbose_name": "Attendance",
                "verbose_name_plural": "Attendances",
                "db_table": "attendance",
                "ordering": ["-created_at"],
            },
        ),
    ]
