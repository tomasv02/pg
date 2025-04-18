#18.04.2025 VRBAT - filtr na úpravu cen, rozdělování řádů
from django import template
register = template.Library()

@register.filter
def price_number(value):
    try:
        value = float(value)
        parts = f"{value:,.2f}".split(".")
        integer_part = parts[0].replace(",", " ").replace(".", " ")
        decimal_part = parts[1]
        return f"{integer_part},{decimal_part}"
    except (ValueError, TypeError):
        return value