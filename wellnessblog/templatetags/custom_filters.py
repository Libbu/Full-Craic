from django import template

register = template.Library()

@register.filter
def get_range(value):
    if value is None:
        return range(0)
    return range(value)


@register.filter
def get_complement_range(value):
    if value is None:
        return range(5)
    return range(5 - value)