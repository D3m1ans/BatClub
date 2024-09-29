from django import template

register = template.Library()

@register.filter(name='split_hero')
def split_hero(value, key):
    parts =  value.split(key)
    return parts[1]

@register.filter(name='split_alterego')
def split_alterego(value, key):
    parts = value.split(key)
    return parts[2]