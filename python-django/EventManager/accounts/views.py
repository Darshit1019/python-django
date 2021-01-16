from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Event_Registration, Participant_Registration
import datetime

from .form import EventRegistrationForm, ParticipantRegistrationForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def event_registration(request):
    event = EventRegistrationForm()
    if request.method=="POST":
        event = EventRegistrationForm(request.POST)
        if event.is_valid():
            event.save()
            registered_event = Event_Registration.objects.all().get(event_name = request.POST.get('event_name'))
            send_mail('Event Registration Successful', 
            'Event name: '+request.POST.get('event_name')+'\n'+'Event ID :'+ str(registered_event.id)+'\n\n\n'+'You can now review the participation in your event through our portal.'+'\n\n'+ 'Team : Event Manager', 
            'kyakamhehamara@gmail.com',
            [registered_event.host_email])
            return redirect('/')

    context={'event': event}
    return render(request, 'E_R.html', context)

def participant_registration(request):
    registered_event = Event_Registration.objects.filter(registration_deadline__gte=datetime.datetime.now())
    participant = ParticipantRegistrationForm()
    if request.method == 'POST':
        # if request.POST.get('participation_type') == 'individual':
        #     participant = ParticipantRegistrationForm(request.POST, initial={'numberof_participant':1})
        #     participant.numberof_participant = 1
        participant = ParticipantRegistrationForm(request.POST)
        if participant.is_valid():
            participant.save()
            return redirect('/')
    context = {'registered_event': registered_event, 'participant': participant}
    return render(request, 'P_R.html',context)
