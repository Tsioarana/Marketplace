# Dans votre fichier forms.py

from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control type_msg',
                'placeholder': 'Type your message...',
                'style': 'background-color: rgba(0,0,0,0.3); border:0; color:white; height: 60px; overflow-y: auto;'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajout des classes Bootstrap à chaque champ du formulaire
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    # Surcharge de la méthode __str__ pour personnaliser la représentation en chaîne de la classe
    def __str__(self):
        return self.content
