from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext as _

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('student_id', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'contact_no', 'profile_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'admin', 'regular')}),
        # ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('User Lists', {'fields': ('booklist', 'wishlist')}),
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

    actions = ['make_admin']

    def make_admin(self, request, queryset):
        # Perform the action to make selected users admin
        queryset.update(admin=True)
        queryset.update(is_staff=True)
        self.message_user(request, _('%d user(s) were successfully made admin.' % queryset.count()))

    make_admin.short_description = "Make selected users admin"

admin.site.register(User, CustomUserAdmin)