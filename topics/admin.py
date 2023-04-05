from django.contrib import admin

from .models import Topics

class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Topics, TopicAdmin)
