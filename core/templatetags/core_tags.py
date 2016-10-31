from django import template

from core.models import PortfolioPage

register = template.Library()


@register.inclusion_tag(
    'core/tags/portfolio_item_list.html',
    takes_context=True
)
def portfolio_item_list(context, count=4):
    portfolio_items = PortfolioPage.objects.live().order_by('-date')
    return {
        'portfolio_items': portfolio_items[:count].select_related('main_image'),
        'request': context['request'],
    }
