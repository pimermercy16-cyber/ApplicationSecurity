# Create your views here.
from django.shortcuts import render
from .models import Part
from .forms import SearchForm


def home(request):
    form = SearchForm(request.GET or None)
    parts = Part.objects.all()

    if form.is_valid():
        query = form.cleaned_data["q"]
        parts = Part.objects.filter(name__icontains=query)

    return render(request, "parts/home.html", {
        "form": form,
        "parts": parts,
    })
