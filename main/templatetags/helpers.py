from django import template

register = template.Library()

@register.filter()
def is_active(url,request):
    app_name , url_name = url.split("_")
    app , url = request.resolver_match.url_name.split("_")
    return "active" if (app == app_name and url == url_name) else ""

@register.filter()
def minutes(time):
    return int(time*60)