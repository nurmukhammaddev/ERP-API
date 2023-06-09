# Generated by Django 4.2 on 2023-04-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0003_alter_event_address"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={},
        ),
        migrations.AlterField(
            model_name="event",
            name="address",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="event",
            name="slug",
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateTimeField(),
        ),
        migrations.AlterModelTable(
            name="event",
            table=None,
        ),
    ]
