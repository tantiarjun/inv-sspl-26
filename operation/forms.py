from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['supplier_name', 'item_name', 'quantity']  # Updated fields
        widgets = {
            'supplier_name': forms.Select(attrs={'class': 'form-control'}),  # supplier_name
            'item_name': forms.Select(attrs={'class': 'form-control'}),  # item_name
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'oninput': 'calculateTotal()'}),
        }
