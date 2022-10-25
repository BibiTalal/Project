from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event

User=get_user_model()

class Create_userForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "password":forms.PasswordInput()
        }

class SignupForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True, widget=forms.PasswordInput())
    


class EventForm(forms.ModelForm):
    
    class Meta:
        model= Event
        fields= ["name","image","organiser","num_of_seats","date_of_event",]

    