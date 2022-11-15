from dataclasses import field
from django import forms


from .models import ShipmentModel


class shipmentsForm(forms.ModelForm):
    class Meta:
        model = ShipmentModel
        fields = '__all__'