from urllib import request
from django.db import models
from django.conf import settings
from email.policy import default
from unicodedata import category
from django.contrib.auth import get_user_model


User=get_user_model()

class Event(models.Model):
    class BookingStatus(models.TextChoices):
        booked="yes"
        not_booked="no"

    name = models.CharField(max_length=30)
    image = models.TextField(blank=True,null=True)
    organiser=models.CharField(max_length=50)
    num_of_seats=models.IntegerField()
    date_of_event=models.DateTimeField()
    bokkingstatus = models.CharField(max_length=3, choices=BookingStatus.choices,default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.date_of_event


    def __str__(self):
        return self.name



