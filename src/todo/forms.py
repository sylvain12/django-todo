from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(label='Titre', max_length=255)