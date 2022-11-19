from django import forms
from .models import CatchReceipt, Invoices



class AddCatch(forms.ModelForm):
    class Meta:
        model = CatchReceipt
        fields = '__all__'


class AddInvoices(forms.ModelForm):
    class Meta:
        model = Invoices
        fields = ('date', 'auth' )

