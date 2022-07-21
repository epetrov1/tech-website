from django import forms
from django.forms import ModelForm
from . models import Subsciber

class SubsciberForm(ModelForm):
    class Meta:
        model = Subsciber
        fields = ['email']