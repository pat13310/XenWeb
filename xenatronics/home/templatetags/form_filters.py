from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Ajoute une classe CSS aux widgets d'un champ."""
    return field.as_widget(attrs={"class": css_class})
