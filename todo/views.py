from django.views.generic import ListView,DetailView
from django.shortcuts import render

from todo.models import TodoModel

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
