from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
from .models import Event

class EventAdmin(ModelAdmin):
	model = Event
	menu_order = 500
	menu_icon = "date"
	list_display = ('title', 'datetime')

modeladmin_register(EventAdmin)