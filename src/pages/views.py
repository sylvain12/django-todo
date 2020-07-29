from django.shortcuts import render
from todo.models import Todo

def index(request):
    todos = Todo.objects.all()
    context ={
        'todos': todos
    }
    return render(request, 'pages/index.html', context)
