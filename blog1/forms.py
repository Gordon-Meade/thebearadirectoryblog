from .models import Comment
from django import forms
from .models import ContactForm as ContactFormModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ['name', 'email', 'message']