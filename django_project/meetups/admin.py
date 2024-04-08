from django.contrib import admin

from .models import Meetup, Location, Participant
admin.site.register(Meetup)
admin.site.register(Location)
admin.site.register(Participant)
