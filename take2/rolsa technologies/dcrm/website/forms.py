from decimal import Decimal, InvalidOperation
from django import forms


class CalculateForm(forms.Form):
    distance = forms.DecimalField(min_value=0, max_digits=10, decimal_places=3, required=True)
    consumption = forms.DecimalField(min_value=0, max_digits=6, decimal_places=3, required=True)
    price = forms.DecimalField(min_value=0, max_digits=8, decimal_places=4, required=True)
    emission_factor = forms.DecimalField(min_value=0, max_digits=8, decimal_places=4, required=True)

    def compute(self) -> dict:
        """Compute fuel used (L), cost, and emissions using form.cleaned_data.

        Returns a dict with Decimal values rounded appropriately.
        """
        if not self.is_valid():
            raise ValueError("Form must be valid before computing results")

        d = self.cleaned_data
        # fuel used in litres = distance * consumption / 100
        fuel_used = (d["distance"] * d["consumption"]) / Decimal("100")
        cost = fuel_used * d["price"]
        emissions = fuel_used * d["emission_factor"]

        return {
            "fuel_used": fuel_used.quantize(Decimal("0.0001")),
            "cost": cost.quantize(Decimal("0.01")),
            "emissions": emissions.quantize(Decimal("0.001")),
        }


class BookingForm(forms.Form):
    name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone = forms.CharField(max_length=30, required=False)
    service = forms.CharField(max_length=200, required=False)
    date = forms.DateField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)
