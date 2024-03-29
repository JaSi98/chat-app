from django.contrib import admin

from .models import Message, Chat

class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'author', 'receiver')
    search_fields = ('text',)

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)