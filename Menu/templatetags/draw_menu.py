from django import template
from django.urls import reverse
from ..models import Menu

register = template.Library()


@register.inclusion_tag('Menu/menu.html')
def draw_menu(menu_name=0, parent=0):
    data = Menu.objects.select_related('parent')
    menu = []
    for item in data:
        url = reverse(item.url_name)
        menu.append({
            'id': item.pk,
            'url': url,
            'name': item.name,
            'parent': item.parent_id or 0,
            'active': True if menu_name == item.name else False,
        })
    return {
        'menu': menu,
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }
