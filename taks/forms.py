# forms.py
from django import forms
from .models import Task, Advance


class taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "category", "important"]
        labels = {
            "title": "Título",
            "description": "Descripción",
            "important": "Importante",
            "due_date": "Fecha de vencimiento",
            "category": "Categoría",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un título"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribe una descripción"}),
            "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "important": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "style": "border: 1px solid #000; padding: 5px; border-radius: 5px;"
            })
        }

class AdvanceForm(forms.ModelForm):
    class Meta:
        model = Advance
        fields = ["progress_description"]
        labels = {
            "progress_description": "Descripción del Avance",
        }
        widgets = {
            "progress_description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Describe el progreso de la tarea"
            })
        }
