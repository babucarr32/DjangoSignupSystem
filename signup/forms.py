from .models import signupModel
from django import forms

class signupForm(forms.ModelForm):
    class Meta:
        model = signupModel
        fields = ['username', 'password']
        widget = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }