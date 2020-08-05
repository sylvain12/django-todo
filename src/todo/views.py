from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
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


def error_404_view(request, exception):
    return render(request, 'errors/404.html')


def edit(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")
    print(todo, request.method)
    return render(request, 'todo/edit_todo.html', {'todo': todo})