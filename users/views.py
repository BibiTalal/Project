from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from users.forms import SignupForm, Create_userForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Event
from .forms import EventForm
from users import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User=get_user_model()

def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def create_user(request):
    form=Create_userForm()
    if request.method=="POST":
        form=Create_userForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            user.save()
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return ("an 'invalid login' error message")
    form=Create_userForm()      
    context={"form":form}
    return render(request,"create_user.html",context)

def signout_user(req):
    logout(req)
    return redirect("home")

def signin_user(req):
    form=SignupForm()
    if req.method=="POST":
        form=SignupForm(req.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            auth_user=authenticate(username=username, password=password)
            if auth_user is not None:
                login(req,auth_user)
                return redirect("home")
    context={"form":form}
    return render(req,"signin.html",context)

def get_events(req):
    events=Event.objects.all()
    now = timezone.now()
    future_events = [e for e in events if e.date_of_event >= now]
    _events=[]
    
    for event in future_events:
        
        _events.append(
            {
                "id":event.id,
                "name":event.name,
                "image":event.image,
                "organiser":event.organiser,
                "num_of_seats":event.num_of_seats,
                "date_of_event":event.date_of_event,
                "bokkingstatus":event.bokkingstatus,
                
                
            }
        )
    context={"events":_events}
    return render(req, "event_list.html", context)


def create_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event-list")
        
    context = {
        "form": form,
    }
    if request.user.is_anonymous:
        return redirect("signin")
    
    return render(request, "create_event.html", context)

def get_event(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        "event": {
            "id":event.id,
            "name": event.name,
            "image":event.image,
            "organiser":event.organiser,
            "num_of_seats":event.num_of_seats,
            "date_of_event":event.date_of_event,
                
        }
    }
    return render(request, "event_detail.html", context)






