from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',  'birthday', 'address',
            'postal_code', 'city', 'country', 'phone',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-field p-0.5 focus:outline-none focus: border-b focus:border-blue-500'}),
            'birthday': forms.DateInput(attrs={'type':'date','class': 'input-field p-0.5 focus:outline-none focus: border-b focus:border-blue-500'}),
            'address': forms.Textarea(attrs={'class': 'input-field p-0.5 focus:outline-none focus: border-b focus:border-blue-500','cols':30, 'rows': 1}),
            'postal_code': forms.TextInput(attrs={'class': 'input-field p-0.5 focus:outline-none focus: border-b focus:border-blue-500'}),
            'city': forms.TextInput(attrs={'class': 'input-field p-0.5 focus:outline-none focus: border-b focus:border-blue-500'}),
            'country': forms.TextInput(attrs={'class': 'input-field p-0.5 focus:outline-none focus: border-b focus:border-blue-500'}),
            'phone': forms.TextInput(attrs={'class': 'input-field p-0.5 focus:outline-none focus: border-b focus:border-blue-500'}),
        }
