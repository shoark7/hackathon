from django import template
import re

register = template.Library()

@register.filter(name='number_prettify')
def number_prettify(number):
    number_format = re.compile(r'(\d{3})(\d{4})(\d{4})')
    return number_format.sub(r'\1-\2-\3', number)
