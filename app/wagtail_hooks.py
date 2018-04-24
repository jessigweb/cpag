from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
from .models import Event, Verse

class EventAdmin(ModelAdmin):
	model = Event
	menu_order = 500
	menu_icon = "date"
	list_display = ('title', 'datetime')

class VerseAdmin(ModelAdmin):
	model = Verse
	menu_order = 600
	menu_icon = "openquote"
	list_display = ('verse', 'active')

modeladmin_register(EventAdmin)
modeladmin_register(VerseAdmin)