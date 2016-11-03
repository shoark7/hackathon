from django import template
import re

register = template.Library()

@register.filter(name='number_prettify')
def number_prettify(number):
    return number[:3] + '-' + number[3:7] + '-' + number[7:]
