from django import template
register = template.Library()

@register.filter
def formato_precio(value):
    try:
        return "{:,.0f}".format(value).replace(",", ".")
    except (ValueError, TypeError):
        return value