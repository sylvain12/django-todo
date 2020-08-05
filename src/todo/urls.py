from django.urls import path
from . import views
from .views import TodoDetailView

app_name='todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add_todo'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='detail'),
]