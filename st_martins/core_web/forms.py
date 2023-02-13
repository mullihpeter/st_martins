from django import forms
from django.conf import settings


class ContactForm(forms.Form):
    template_name = 'contact_form.html'

    sender = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)
