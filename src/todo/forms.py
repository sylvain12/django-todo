from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(label='titre', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))