from django.views.generic import ListView
from django.shortcuts import render

from todo.models import TodoModel

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel
