from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with z')

class FormName(forms.Form):
    #name = forms.CharField(validators=[check_for_z])
    name = forms.CharField(help_text='Enter your full name')
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your e-mail again')
    text = forms.CharField(widget=forms.Textarea)
    #botcatcher = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()

        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError('Make sure e-mails match')
