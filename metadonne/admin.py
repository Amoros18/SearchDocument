from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Langue)
admin.site.register(Document)
admin.site.register(Sujet)
admin.site.register(Musique)
admin.site.register(ClipMusicale)
admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Pays)
admin.site.register(TypeDocument)
admin.site.register(Personne)
