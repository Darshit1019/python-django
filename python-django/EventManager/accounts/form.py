from django import forms
from django.forms import ModelForm
from .models import Event_Registration , Participant_Registration
import datetime
from phonenumber_field.formfields import PhoneNumberField


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)

class EventRegistrationForm(forms.ModelForm):
	class Meta:
		widgets = {'event_name': forms.TextInput(attrs={'placeholder': 'Event Name', 'class':'event_name_input'}),
		 'description': forms.Textarea(attrs={'placeholder': 'Description Here', 'class': 'description_input '}),
		 'location': forms.TextInput(attrs={'placeholder': 'Location', 'class':'location_input'}),
		 'starting_date': DateTimeInput(attrs={'class': 'date-time_input_E_R ', 'class': 'datetime_input_from '}), 
		 'ending_date': DateTimeInput(attrs={'class': 'date-time_input_E_R ', 'class': 'datetime_input_to '}), 
		 'registration_deadline': DateTimeInput(attrs={'class': 'date-time_input_E_R ', 'class': 'datetime_input_regdeadline '}), 
		 'host_email': forms.TextInput(attrs={'placeholder': 'Host Email', 'class':'host_email_input'}),
		 'host_password': forms.PasswordInput(attrs={'placeholder': 'Host Password'})
		 }
		model = Event_Registration
		fields = '__all__'

class ParticipantRegistrationForm(forms.ModelForm):
	events = forms.ModelMultipleChoiceField(queryset=Event_Registration.objects.filter(registration_deadline__gte=datetime.datetime.now()),
	 required=False,
	  widget=forms.CheckboxSelectMultiple())
	CHOICES = [
        ('individual','individual'),
        ('group','group'),
    ]
	participation_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	numberof_participant = forms.IntegerField(required=False, widget = forms.NumberInput(attrs={'placeholder' : 'Number of Participant','class' : 'numberof_participant_input'}))

	class Meta:
		widgets = {'participant_name' : forms.TextInput(attrs={'placeholder': 'Participant Name','class': 'participant_name_input'}),
		'contact_no': forms.TextInput(attrs={'placeholder': 'Contact Number', 'class':'contact_no_input'}),
		'participant_email': forms.TextInput(attrs={'placeholder': 'Participant Email', 'class':'participant_email_input'}),
		}
		model = Participant_Registration
		fields = '__all__'