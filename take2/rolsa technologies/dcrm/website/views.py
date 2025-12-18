from decimal import Decimal
from typing import Any, Dict

from django.shortcuts import render
from django.http import HttpRequest

from .forms import CalculateForm, BookingForm


def home(request: HttpRequest):
    """Render the site home page."""
    return render(request, "index.html")


def calculate(request: HttpRequest) -> Any:
    """Handle the emissions & cost calculator using a Django Form for validation.

    Uses POSTed form values and returns computed results in the template context.
    """
    context: Dict[str, Any] = {}

    if request.method == "POST":
        form = CalculateForm(request.POST)
        if form.is_valid():
            results = form.compute()
            context.update({"form": form, **results})
        else:
            context["form"] = form
    else:
        # Provide sensible defaults for the GET form
        form = CalculateForm(
            initial={"distance": 0, "consumption": 0, "price": 0, "emission_factor": Decimal("2.31")}
        )
        context["form"] = form

    return render(request, "calculate.html", context)


def booking(request: HttpRequest) -> Any:
    """Handle a simple booking request with validation via a Django Form.

    Does not persist data; returns a success flag and the submitted data on success.
    """
    context: Dict[str, Any] = {}

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            context["success"] = True
            context["submitted"] = form.cleaned_data
        else:
            context["form"] = form
    else:
        context["form"] = BookingForm()

    return render(request, "booking.html", context)