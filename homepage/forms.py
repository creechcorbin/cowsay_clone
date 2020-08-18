from django import forms
import subprocess

class InputForm(forms.Form):
    text = forms.CharField(max_length=100)

