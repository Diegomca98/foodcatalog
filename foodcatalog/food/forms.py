from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_price', 'item_description', 'item_image']
        labels = {
            'item_name' : 'Name',
            'item_price' : 'Price',
            'item_description' : 'Description',
            'item_image' : 'Image',
        }