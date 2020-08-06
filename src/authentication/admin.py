from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Account', {'fields': ['username', 'email', 'password']}),
        ('Indentification', {'fieds': ['first_name', 'last_name', 'email']}),
    ]


admin.site.register(User, UserAdmin)