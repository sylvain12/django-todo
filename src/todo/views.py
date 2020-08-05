from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.core.mail import send_mail, send_mass_mail, EmailMessage

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



# def detail(request, question_id):
#     todo = Todo.objects.get(pk=)
class TodoDetailView(DetailView):
    model = Todo
    template_name='todo/detail.html'
    context_object_name='todo'
    
    def get_queryset(self):
        self.todo = get_object_or_404(Todo, pk=self.kwargs['pk'])
        return Todo.objects.filter(pk=self.todo.pk)
    

@login_required(login_url='/account/login')
def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        
        if form.is_valid():
            form_title = form.cleaned_data['title']
            todo = Todo()
            todo.title = form_title
            todo.save()

            subject = 'Todo created'
            message = f'''
            the user {request.user.username} has created a todo
        '''
            recipients = [request.user.email]
            from_email='sylvainka12@gmail.com'
            
            send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipients)
            return HttpResponseRedirect('/')


    form = TodoForm()
    return render(request, 'todo/add_todo.html', {'form': form})