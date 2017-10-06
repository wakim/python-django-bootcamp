from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data['username']
        email = cleaned_data['email']

        if len(email) == 0:
            raise forms.ValidationError({'email': 'Enter the e-mail'})
        elif User.objects.filter(email = email).exclude(username = username).exists():
            raise forms.ValidationError({'email': 'Email addresses must be unique.'})
