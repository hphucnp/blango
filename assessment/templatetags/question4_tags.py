from django import template

register = template.Library()


@register.inclusion_tag('comments.html')
def comments_for_thing(thing):
    return {'comments': thing.comments.order_by('content')}