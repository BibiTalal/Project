# Generated by Django 4.1.2 on 2022-10-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_delete_booking"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="bokkingstatus",
            field=models.CharField(
                choices=[("yes", "Booked"), ("no", "Not Booked")],
                default=True,
                max_length=3,
            ),
        ),
    ]
