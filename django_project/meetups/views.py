from django.shortcuts import render

def index(request):
    meetups = [
        {
        'title': 'A First Meetup',
        'location': 'New York',
        'slug': 'a-first-meetup'
        },
        {
        'title': 'A Second Meetup',
        'location': 'Paris',
        'slug': 'a-second-meeetup'
        }
        ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'varmeetups': meetups
        })