from django.urls import path
from . import views

app_name='todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todos_list, name='todos_list'),
    path('todos/add', views.add, name='add'),
]