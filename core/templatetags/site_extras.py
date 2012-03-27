from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy
from django.conf import settings
from django import template
import re

register = template.Library()

def site_name():
	return ugettext_lazy(Site.objects.get(id=settings.SITE_ID).name)
register.simple_tag(site_name)

def site_domain():
	return Site.objects.get(id=settings.SITE_ID).domain
register.simple_tag(site_domain)

def site_version():
	return "v=" + str(settings.VERSION)
register.simple_tag(site_version)

@register.filter
def mod(value, arg):
    return value % arg