from django.contrib import admin
from .models import Conversation, ConversationMessage
# Register your models here.

admin.site.register(ConversationMessage)
admin.site.register(Conversation)
