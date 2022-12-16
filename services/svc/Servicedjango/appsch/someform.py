from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['picture', 'name', 'about_item', 'price']

