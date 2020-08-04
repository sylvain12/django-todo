from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect

CRITICAL = 60

def register(request):
    if request.method == 'POST':
        form_data = request.POST

        first_name = form_data['first_name']
        last_name = form_data['last_name']
        username = form_data['username']
        email = form_data['email']
        password = form_data['password']
        confirm_password = form_data['password_confirm']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username taken...')
                return redirect('/account/register/')
            elif User.objects.filter(email=email).exists():
                messages.add_message(request, messages.ERROR, 'Email taken...')
                return redirect('/account/register/')
            else:
                User.objects.create_user(first_name=first_name, 
                last_name=last_name, username=username, email=email, password=password)

        else:
            messages.add_message(request, messages.ERROR, 'Password not matching')
            return redirect('/account/register/')

        messages.add_message(request, messages.SUCCESS, 'User registration successfully...')
        return HttpResponseRedirect('/')

    return render(request, 'authentication/register.html')



def login(request):
    if request.method=='POST':
        form_data = request.POST
        username = form_data['username']
        password = form_data['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.INFO, 'Bienvenue vous etes connecté')
            return redirect('/')
        else:
            messages.add_message(request, CRITICAL, 'Username or password incorrect...')
            return HttpResponseRedirect('/account/login/')

    else:
        return render(request, 'authentication/login.html')


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, 'Merci, vous etes deconnecté...')
    return redirect('/')