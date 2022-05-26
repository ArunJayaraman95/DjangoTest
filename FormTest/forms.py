from django.forms import ModelForm
from .models import CartoonEntry
from django.db import models
from django import forms

class CartoonForm(ModelForm):
    class Meta:
        model = CartoonEntry
        fields = ("cartoon_name", "episode_count", "date_finished", "rating")
        widgets = {
            "cartoon_name": forms.TextInput(attrs={}),
            "episode_count": forms.NumberInput(attrs={"min": 1}),
            "date_finished": forms.DateTimeInput(attrs={"type":"datetime-local", "value": "2000-01-01T12:00"}),
            "rating": forms.NumberInput(attrs={"min": 0, "max": 10, "step": 0.1})
        }