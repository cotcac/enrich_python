from django.contrib import admin

from .models import Topics

class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Topics, TopicAdmin)
