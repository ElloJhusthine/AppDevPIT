# todo/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Task  # Import Task model from models.py

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'  # Path to the template to render the task list
    context_object_name = 'tasks'  # Name of the context variable in the template
