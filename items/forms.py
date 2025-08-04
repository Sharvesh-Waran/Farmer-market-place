from django import forms

from .models import Transaction

class NewTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('name', 'price', 'quantity')