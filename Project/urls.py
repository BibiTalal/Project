"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from users.views import  create_event, home, create_user, signin_user,signout_user,get_events,get_event,done_booking,profile_update
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from users.views import ChangePasswordView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home, name="home"),
    path("signup/",create_user,name="create-user"),
    path("signout/",signout_user,name="signout"),
    path("signin/",signin_user,name="signin"),
    path("events/",get_events,name="event-list"),
    path("add/event/",create_event,name="create-event"),
    path("event/<int:event_id>/", get_event, name="event-detail"),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path("done/<int:done_id>/",done_booking,name="done"),
    path("profile/update/",profile_update,name="profile-update"),
    path("password/change/", ChangePasswordView.as_view(), name="change-password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
