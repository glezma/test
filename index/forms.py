from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control',
                                    'placeholder':'Password...' }))
    username = forms.EmailField(widget = forms.EmailInput(attrs={'type':'text','class':'form-control',
                                    'placeholder':'E-Mail...' }))
    lastname = forms.CharField(widget =forms.TextInput(attrs={'type':'text','class':'form-control',
                                    'placeholder':'Last Name...' }))
    firstname = forms.CharField(widget =forms.TextInput(attrs={'type':'text','class':'form-control',
                                    'placeholder':' Name...' }))

    class Meta:
        model = User
        fields = [ 'username','password','lastname', 'firstname']

class LoginForm(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control',
                                    'placeholder':'Password...' }))
    username = forms.EmailField(widget = forms.EmailInput(attrs={'type':'text','class':'form-control',
                                    'placeholder':'E-Mail...' }))

    class Meta:
        model = User
        fields = [ 'username','password']