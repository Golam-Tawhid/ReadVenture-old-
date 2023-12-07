from django import template
from django.contrib.messages import get_messages
from django.http import request


register = template.Library()

@register.simple_tag
def display_messages():
    messages = get_messages(request)
    return messages
