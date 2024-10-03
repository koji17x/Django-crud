from django.contrib import admin
from .models import Task, Advance  # Asegúrate de importar tu modelo Advance

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

class AdvanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'progress_description', 'task')  # Campos que deseas mostrar en la lista
    search_fields = ('progress_description',)  # Permite buscar por descripción de avance
    list_filter = ('task',)  # Permite filtrar por tarea

# Registro de los modelos en el panel de administración
admin.site.register(Task, TaskAdmin)
admin.site.register(Advance, AdvanceAdmin)  # Registra el modelo Advance
