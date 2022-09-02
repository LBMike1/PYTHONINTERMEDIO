from django.forms import ModelForm
from .models import Owner
from django import forms


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


# class OwnerForm(forms.Form):
#     nombre = forms.CharField(max_length=40)
#     edad = forms.IntegerField(max_value=100)
#     pais = forms.CharField(max_length=20)
