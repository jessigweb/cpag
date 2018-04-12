from datetime import date
from django import template

from app.models import Event 

register = template.Library()

@register.simple_tag()
def get_events():
	return Event.objects.filter(active=True).order_by('datetime')