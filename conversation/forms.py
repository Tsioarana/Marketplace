from django import forms
from .models import Conversation, ConversationMessage

class ConversationMessageForm(forms.ModelForm):
  class Meta:
    model = ConversationMessage
    fields = ('content',)
    widget = {
        'centent': forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 4
      })
    }