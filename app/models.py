from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel, StreamFieldPanel
)

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
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

class Verse(models.Model):
    verse = models.CharField(max_length=200)
    text = models.TextField()
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    panels = [
        FieldPanel('verse'),
        FieldPanel('text'),
        FieldPanel('active')
    ]

MISSION_AREA = (
    ('HOME', 'Home'),
    ('FOREIGN', 'Foreign'),
)

class Mission(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True)
    area = models.CharField(
        max_length=200,
        choices=MISSION_AREA,
        default='HOME',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )

    def __unicode__(self):
        return self.name

    panels = [
        FieldPanel('name'),
        FieldPanel('link'),
        FieldPanel('area'),
        ImageChooserPanel('image')
    ]


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
        FieldPanel('featured'),
        FieldPanel('active')
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

"""Form Models"""
class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

"""Page Models"""
class HomePage(Page):
    pass

class EventPage(Page):
    pass

class GivingPage(Page):
    pass

class StandardPage(Page):
	body = StreamField([
        ('heading', HeadingBlock(required=False)),
        ('paragraph', blocks.RichTextBlock(required=False)),
        ('html', RawHTMLBlock(required=False)),
        ('staff', StaffBlock(required=False)),
        ('image', ImageBlock(required=False)),
        ('mission', ChoiceBlock(choices=[
            ('HOME', 'Home'),
            ('FOREIGN', 'Foreign')
            ], icon='site', required=False))
    ])

	content_panels = Page.content_panels + [
	    StreamFieldPanel('body'),
	]
