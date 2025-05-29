from django import forms

from .models import Link

class Linkform(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name', 'url', 'slug']