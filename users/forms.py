from tabnanny import check
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event

User=get_user_model()

class CreateUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "password":forms.PasswordInput()
        }

class SigninForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True, widget=forms.PasswordInput())
    


class EventForm(forms.ModelForm):
    
    class Meta:
        model= Event
        fields= ["name","image","num_of_seats","date_of_event"]

        def __init__(self):
            if check():
                self.fields['booking_status'].initial=True

    