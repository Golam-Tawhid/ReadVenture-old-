from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('student_id', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'contact_no', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'admin', 'regular', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_id', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('student_id', 'email', 'first_name', 'last_name', 'is_staff', 'admin', 'regular')
    list_filter = ('is_staff', 'admin', 'regular')
    search_fields = ('student_id', 'email', 'first_name', 'last_name')
    ordering = ('student_id',)

admin.site.register(User, CustomUserAdmin)
