from django import template
from django.forms import fields

register = template.Library()

@register.filter(name='css_class')
def css_class(field, class_name):
    '''Adds a css class to a given form field'''
    allowed_field_classes = (
        fields.BoundField,
        fields.Field,
    )
    if not isinstance(field, allowed_field_classes):
        raise AttributeError('field must be an instance of django.forms.fields.Field')

    return field.as_widget(attrs={'class': class_name})