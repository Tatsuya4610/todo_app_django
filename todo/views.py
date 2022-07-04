from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from django.shortcuts import render

from todo.models import TodoModel

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title','memo','priority','date')
    # reverse_lazyはtodo/urls.py内のname='list'に紐付け、POST成功時にそのViewへ遷移させる。
    success_url = reverse_lazy('list')
