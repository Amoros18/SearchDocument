from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Langue)
admin.site.register(Utilisateur)
admin.site.register(Document)
admin.site.register(Sujet)
