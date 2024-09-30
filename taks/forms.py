from django import forms
from .models import Task


class taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        labels = {
            "title": "Título",
            "description": "Descripción",
            "important": "Importante",
            "due_date": "Fecha de vencimiento",
            "category": "Categoria",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un título"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribe una descripción"}),
            "due_date": forms.DateTimeInput(attrs={ "class": "form-control", "placeholder": "Tiempo de vencimiento"}),
            "status" : forms.TextInput(attrs={"class": "form-control", "placeholder": "Categoria"}),
            "important": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "style": "border: 1px solid #000; padding: 5px; border-radius: 5px;"
            })
        }