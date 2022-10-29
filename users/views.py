from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from users.forms import SigninForm, CreateUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Event
from .forms import EventForm
from django.contrib import messages
from users import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
User=get_user_model()




def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def create_user(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            user.save()
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return ("an 'invalid login' error message")     
    context={"form":form}
    return render(request,"create_user.html",context)

def signout_user(req):
    logout(req)
    return redirect("home")

def signin_user(req):
    form=SigninForm()
    if req.method=="POST":
        form=SigninForm(req.POST)
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
    datetime = timezone.now()
    events=Event.objects.filter(date_of_event__gte = datetime.today())
    
    _events=[]
    
    for event in events:
        
        _events.append(
            {
                "id":event.id,
                "name":event.name,
                "image":event.image,
                "organiser":event.organiser,
                "num_of_seats":event.num_of_seats,
                "date_of_event":event.date_of_event,
                
                
                
            }
        )
    context={"events":_events}
    return render(req, "event_list.html", context)


def create_event(request):
    if request.user.is_anonymous:
        return redirect("signin")
    
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            events=form.save(commit=False)
            events.organiser=request.user
            events.save()
            return redirect("event-list")
        
    context = {
        "form": form,
    }
    
    return render(request, "create_event.html", context)

def get_event(request, event_id):
    event = Event.objects.get(id=event_id)
    # user_count=User.objects.annotate=Count('bookingstatus',filter=Q(bookingstatus="yes"))
    context = {
        "event": {
            "id":event.id,
            "name": event.name,
            "image":event.image,
            "organiser":event.organiser,
            "num_of_seats":event.num_of_seats,
            "date_of_event":event.date_of_event, 
            "booking_status":event.booking_status,
            "num_of_seats_booked":event.num_of_seats_booked,
            }
                
        
    }
    return render(request, "event_detail.html", context)


def done_booking(request, done_id):
    done = Event.objects.get(id=done_id)
    # user_count=User.objects.annotate=Count('bookingstatus',filter=Q(bookingstatus="yes"))
    context = {
        "done": {
            "id":done.id,
            "name": done.name,
            "date_of_event":done.date_of_event, 
           
            }
                
        
    }
    return render(request, "done.html", context)


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile-update')
    else:
        user_form = UpdateUserForm(instance=request.user)
        

    return render(request, 'profile_update.html', {'user_form': user_form})



class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "change_password.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


    



