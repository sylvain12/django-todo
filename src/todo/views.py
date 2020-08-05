from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required


# ERRORS PAGES
def error_404_view(request, exception):
    return render(request, 'errors/404.html')

def error_500_view(request):
    return render(request, 'errors/500.html')

def index(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)



@login_required(login_url='/account/login')
def add(request):

    if request.method == 'POST':
        form = TodoForm(request.POST)
        
        if form.is_valid():
            form_title = form.cleaned_data['title']
            todo = Todo()
            todo.title = form_title
            todo.save()

            return HttpResponseRedirect('/')


    form = TodoForm()
    return render(request, 'todo/add_todo.html', {'form': form})