from django import forms

from sweetshop.contact.models import ContactForm


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message'})
        }
