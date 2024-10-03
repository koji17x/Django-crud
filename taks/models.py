from django.db import models
from django.contrib.auth.models import User

# Modelo Task que ya tienes definido
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datacompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title + " - by " + self.user.username

# Nuevo modelo Advance relacionado foráneamente con Task
class Advance(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='advances')  # Relación con Task
    progress_description = models.TextField()  # Descripción del avance
    date = models.DateTimeField(auto_now_add=True)  # Fecha de registro del avance

    def __str__(self):
        return f"Avance de {self.task.title} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
