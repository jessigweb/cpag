from datetime import date
from django import template

from app.models import Event, Verse , Mission

register = template.Library()

@register.simple_tag()
def get_events():
	return Event.objects.filter(active=True).order_by('datetime')

@register.simple_tag()
def get_verse():
	verses = Verse.objects.filter(active=True)
	verses = verses[0]
	return 

@register.simple_tag()
def get_featured_events():
	events = Event.objects.filter(featured=True).order_by('datetime')
	events = events[0]
	return events

@register.simple_tag()
def get_missions(category):
	return Mission.objects.filter(area=category)