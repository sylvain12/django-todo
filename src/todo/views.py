from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import TodoForm

def index(request):
    return redirect('todos/')


def todos_list(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)


def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            todo = Todo()
            todo.title = title
            todo.save()
            return HttpResponseRedirect('/')
    
    form = TodoForm()
    return render(request, 'todo/add_todo.html', {'form': form})