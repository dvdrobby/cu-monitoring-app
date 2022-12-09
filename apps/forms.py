from django.forms import forms
from django.forms import ModelForm

from .models import FormModel

class FormForm(ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'