# Generated by Django 4.1.2 on 2022-10-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_remove_event_user_delete_signin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="organiser",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
