from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django_select2.forms import Select2Widget

from .models import GENDER_CHOICES, BLOOD_GROUP_CHOICES
from .models import BecomeDonor

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BecomeDonorForm(forms.ModelForm):
    class Meta:
        model = BecomeDonor
        fields = '__all__'
        labels = {
            'phn_no': "Mobile Number",
            'blood_group': "Blood Group"
        }
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))