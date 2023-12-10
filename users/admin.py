from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import FormUserChange, CreateUserForm


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CreateUserForm
    form = FormUserChange
    model = User
    list_display = ['phone', 'is_active', 'is_staff']
    list_filter = ['phone']
    fieldsets = [
        (None, {'fields': ['phone', 'password']}),
        ('Personal info', {'fields': ['first_name', 'last_name']}),
        ('Permission', {'fields': ['is_staff']})
    ]

    add_fieldsets = [
        (
            None,
            {
                'fields': ['phone', 'password1', 'password2']
            },
        ),
    ]
    search_fields = ['phone']
    ordering = ['phone']


admin.site.register(User, CustomUserAdmin)
