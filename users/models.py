from urllib import request
from django.db import models
from django.conf import settings
from email.policy import default
from unicodedata import category
from django.contrib.auth import get_user_model

User=get_user_model()

class Event(models.Model):
    
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True,null=True)
    num_of_seats_booked=models.IntegerField(blank=True, null=True)
    organiser=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="events")
    num_of_seats=models.IntegerField()
    date_of_event=models.DateField()
    booking_status = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    


    def __str__(self):
        return self.name



