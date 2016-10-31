from django.db import models
import datetime

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class HomePage(Page):
    pass


class PortfolioIndexPage(Page):
    description = RichTextField("Description")

    content_panels = Page.content_panels + [
        FieldPanel('description')
    ]

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        context['portfolio_items'] = PortfolioPage.objects.order_by('date')
        return context


class PortfolioPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    date = models.DateField(("Post date"), default=datetime.date.today)
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('html', blocks.RawHTMLBlock(icon='site', label='Raw HTML'))
    ])

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body')
    )

    @property
    def portfolio_index(self):
        return self._get_ancestors().type(PortfolioIndexPage).last()

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('date'),
        FieldPanel('intro', classname="full"),
        StreamFieldPanel('body'),
    ]
