from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
from .models import Event, Verse, Mission

class EventAdmin(ModelAdmin):
	model = Event
	menu_order = 500
	menu_icon = "date"
	list_display = ('title', 'datetime', 'featured')
	list_editable = ('featured')

class MissionAdmin(ModelAdmin):
	model = Mission
	menu_order = 700
	menu_icon = "site"
	list_display = ('name', 'area', 'link')

class VerseAdmin(ModelAdmin):
	model = Verse
	menu_order = 600
	menu_icon = "openquote"
	list_display = ('verse', 'active')

modeladmin_register(EventAdmin)
modeladmin_register(VerseAdmin)
modeladmin_register(MissionAdmin)