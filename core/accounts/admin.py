from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['email', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['email']
    ordering = ['email']
    
    fieldsets = (
        ('Informations', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}),
        ('group Permissions', {'fields': ['groups', 'user_permissions']}),
        ('important date', {'fields': ['last_login']}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}),
    )
