from django.contrib import admin
from users import models

to_register=[models.Event]
admin.site.register(to_register)

