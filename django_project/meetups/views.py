from django.shortcuts import render

def index(request):
    meetups = [
        {
        'title': 'A First Meetup',
        'location': 'New York',
        'slug': 1
        },
        {
        'title': 'A Second Meetup',
        'location': 'Paris',
        'slug': 2
        }
        ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
        })

def meetup_details(request, meetup_slug):
    selected_meetup = [{
        'title': 'A First Meetup',
        'description': 'This is the first meetup!'
        },
        {
        'title': 'A Second Meetup',
        'description': 'This is the second meetup!'
        }
        ]
    numb=int(meetup_slug)-1

    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup[numb]['title'],
        'meetup_description': selected_meetup[numb]['description']
        })