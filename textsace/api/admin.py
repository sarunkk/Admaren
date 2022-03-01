import imp
from django.contrib import admin

from api.models import Snippet, Tag
# Register your models here.

admin.site.register(Snippet)
admin.site.register(Tag)