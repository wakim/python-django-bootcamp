from django import template

register = template.Library()

@register.filter(name='cutting')
def cutting(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')
