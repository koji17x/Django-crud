from django.contrib import admin
from .models import Task, Advance


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

class AdvanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'progress_description', 'task')
    search_fields = ('progress_description',)
    list_filter = ('task',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Advance, AdvanceAdmin)
