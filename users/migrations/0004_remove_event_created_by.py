# Generated by Django 4.1.2 on 2022-10-24 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_event_bokkingstatus"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="created_by",
        ),
    ]
