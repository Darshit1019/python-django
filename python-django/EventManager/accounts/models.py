from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Event_Registration(models.Model):
    event_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    starting_date = models.DateTimeField(null=True)
    ending_date = models.DateTimeField(null=True)
    registration_deadline = models.DateTimeField(null=True)
    host_email = models.EmailField(null=True)
    host_password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.event_name

class Participant_Registration(models.Model):
    CHOICES = [
        ('individual','individual'),
        ('group','group'),
    ]
    participant_name = models.CharField(max_length=200, null=True, blank=True)
    contact_no = models.CharField(max_length=200, null=True, blank=True)
    participant_email = models.EmailField(null=True)
    events = models.ManyToManyField(Event_Registration)
    participation_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    numberof_participant = models.PositiveSmallIntegerField(blank=True,null=True)

    def __str__(self):
        return self.participant_name


