# Import necessary modules
from django.shortcuts import render
from django.views.generic import ListView
from todo.models import Task  # Correctly import Task from the 'todo' app

# Class-based view for displaying tasks
class TaskListView(ListView):
    model = Task  # Set the model to Task from 'todo' app
    template_name = 'task_list.html'  # Specify the template to render
    context_object_name = 'tasks'  # The context variable used in the template to access the tasks

# If you want a simple home page, you can define it here too
def home(request):
    return render(request, 'home.html')  # You need a 'home.html' template for this to work
