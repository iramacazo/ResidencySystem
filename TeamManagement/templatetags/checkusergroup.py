from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user):
    group = Group.objects.get()
    return True if group in user.groups.all() else False
