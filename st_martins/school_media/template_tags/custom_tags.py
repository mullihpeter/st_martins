from django import template
from st_martins.school_media.models import Videos



register = template.Library()


# An upper function that capitalizes the first letter of a string.
@register.filter(name='capitalize')
def capitalize(value):
    return value[0].upper() + value[1:]


# An upper function that sets returns a red color. We then register the filter using a suitable name.
@register.filter(name='get_color')
def color(value):
    if value:
        return "#FF0000"


# Create  latest 4 show_videos filter tag that will return all videos and register them.
@register.filter(name='latest_videos')
def latest_videos(value):
    return Videos.objects.all()[:4]


# Create  latest 4 show_videos filter tag that will return all videos and register them.
