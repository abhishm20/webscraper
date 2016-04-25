from django import forms
from .models import User, Alert
from django.db import models
from datetime import datetime
from django.utils import timezone


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobile', 'password']

class Update(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

class UpdateImage(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['url', 'name', 'exp_to', 'exp_from', 'act_price', 'user']
