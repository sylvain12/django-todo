from django.shortcuts import render
from .models import Todo

def index(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)
