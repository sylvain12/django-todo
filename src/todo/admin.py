from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['title']}),
        ('Test', {'fields': ['is_conpleted']})
    ]

    list_display = ('title', 'is_conpleted')
    list_filter = ['is_conpleted']
    search_fields = ['title', 'is_conpleted']
    # fields = ['title', 'is_conpleted']


admin.site.register(Todo, TodoAdmin)
