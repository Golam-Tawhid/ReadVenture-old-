from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Books, Receipt

# class BooksAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'isbn', 'genre', 'category', 'language', 'user_student_id']
#     search_fields = ['title', 'author', 'isbn', 'genre', 'category', 'language', 'user__student_id']
#     list_filter = ['genre', 'category', 'language']

#     def user_student_id(self, obj):
#         return obj.user.student_id if obj.user else ''
#     user_student_id.short_description = 'User Student ID'

# admin.site.register(Books, BooksAdmin)





class CustomUserAdmin(UserAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email', 'admin', 'regular')
    list_filter = ('admin', 'regular')
    search_fields = ('student_id', 'email', 'first_name', 'last_name')
    ordering = ('student_id',)

    fieldsets = (
        (None, {'fields': ('student_id', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'contact_no', 'profile_picture')}),
        ('Permissions', {'fields': ('admin', 'regular', 'booklist', 'wishlist')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_id', 'password1', 'password2'),
        }),
    )

admin.site.register(User, CustomUserAdmin)



