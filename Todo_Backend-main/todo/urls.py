from django.urls import path
from . import views  # Ensure you're importing views from the todo app

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),  # Ensure it's not circular
]
