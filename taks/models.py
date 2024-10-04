from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class CategoryChoices(models.TextChoices):
        WORK = 'WRK', 'Trabajo'
        STUDY = 'STD', 'Estudio'
        PERSONAL = 'PER', 'Personal'
        OTHER = 'OTH', 'Otro'

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datacompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True, blank=True)
    category = models.CharField(
        max_length=3,
        choices=CategoryChoices.choices,
        default=CategoryChoices.OTHER,
    )

    def __str__(self):
        return self.title + " - by " + self.user.username

class Advance(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='advances')
    progress_description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avance de {self.task.title} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
