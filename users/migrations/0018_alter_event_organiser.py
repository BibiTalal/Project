# Generated by Django 4.1.2 on 2022-10-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0017_alter_event_date_of_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="organiser",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
