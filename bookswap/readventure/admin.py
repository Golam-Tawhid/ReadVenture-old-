from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Books, Receipt

class CustomUserAdmin(UserAdmin):
    # Existing fields and configurations...

    fieldsets = (
        # Existing fieldsets...
        (
            'Wishlist',
            {
                'fields': ('wishlist',),  # Add 'wishlist' field here
            },
        ),
    )


# class CustomUserAdmin(UserAdmin):
#     list_display = ('student_id', 'first_name', 'last_name', 'email', 'admin', 'regular')
#     list_filter = ('admin', 'regular')
#     search_fields = ('student_id', 'email', 'first_name', 'last_name')
#     ordering = ('student_id',)

#     fieldsets = (
#         (None, {'fields': ('student_id', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'contact_no', 'profile_picture')}),
#         ('Permissions', {'fields': ('admin', 'regular', 'booklist', 'wishlist')}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('student_id', 'password1', 'password2'),
#         }),
#     )

# admin.site.register(User, CustomUserAdmin)



