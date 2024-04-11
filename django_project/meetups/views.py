from django.shortcuts import render, redirect
from .models import Meetup, Participant
from .forms import RegistrationForm

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
        })

def meetup_details(request, meetup_slug):

    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_name = registration_form.cleaned_data['name']
                user_email = registration_form.cleaned_data['email']
                user_address = registration_form.cleaned_data['address']
                instance, _ = Participant.objects.get_or_create(name=user_name, email=user_email, address=user_address)
                selected_meetup.participants.add(instance)
                return redirect('confirm-registration', meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
            })

    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
            })
    
def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug) 
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
        })

