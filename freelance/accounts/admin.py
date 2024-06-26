from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


user = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = user
    list_display = [
        'email', 'first_name', 'last_name', 'is_freelancer', 'experience'
        ]


admin.site.register(user, CustomUserAdmin)
