# todo/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, default="Untitled Task")  # Add default value
    description = models.TextField(default="No description")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
