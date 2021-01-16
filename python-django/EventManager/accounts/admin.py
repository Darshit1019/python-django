from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Event_Registration)
admin.site.register(Participant_Registration)