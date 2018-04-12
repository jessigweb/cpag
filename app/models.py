from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.blocks import (
    TextBlock, 
    StructBlock, 
    StreamBlock, 
    FieldBlock, 
    CharBlock, 
    RichTextBlock, 
    RawHTMLBlock, 
    ChoiceBlock, 
    ChooserBlock,
    URLBlock, 
    IntegerBlock, 
    PageChooserBlock
)

class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )
    datetime = models.DateTimeField()
    summary = RichTextField()
    active = models.BooleanField(default=True)
    featured = models.BooleanField(blank=True)

    def __unicode__(self):
        return self.title

    class Meta: 
        ordering = ['datetime']

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        FieldPanel('datetime'),
        FieldPanel('summary'),
        FieldPanel('featured')
    ]

"""StreamField Blocks"""

class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], 
        blank=True, 
        initial='h1')

    class Meta:
        icon = "title"

class StaffBlock(StructBlock):
	name = CharBlock(required=True)
	title = CharBlock(required=True)
	image = ImageChooserBlock(required=True)
	content = RichTextBlock(required=True)

	class Meta:
		icon= "group"

class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    formatting = ChoiceBlock(choices=[
        ('', 'Select a image format'),
        ('original', 'Original'),
        ('banner', 'Banner'),
        ('custom', 'Custom')
    ], 
        blank=True, 
        initial='original')
    width = CharBlock(required=False)
    height = CharBlock(required=False)

    class Meta:
        icon = "image"


"""Page Models"""
class HomePage(Page):
    pass

class EventPage(Page):
    pass

class StandardPage(Page):
	body = StreamField([
        ('heading', HeadingBlock(required=False)),
        ('paragraph', blocks.RichTextBlock(required=False)),
        ('html', RawHTMLBlock(required=False)),
        ('staff', StaffBlock(required=False)),
        ('image', ImageBlock(required=False)),
    ])

	content_panels = Page.content_panels + [
	    StreamFieldPanel('body'),
	]
