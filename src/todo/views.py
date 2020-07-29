from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    return redirect('todos/')


def todos_list(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)


def add(request):
    pass