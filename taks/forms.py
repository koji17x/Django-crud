from django import forms
from .models import Task


class taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        labels = {
            "title": "Título",
            "description": "Descripción",
            "important": "Importante"
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un título"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribe una descripción"}),
            "important": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "style": "border: 1px solid #000; padding: 5px; border-radius: 1px;"
            })
        }
