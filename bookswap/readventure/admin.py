from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'genre', 'category', 'language', 'user_student_id']
    search_fields = ['title', 'author', 'isbn', 'genre', 'category', 'language', 'user__student_id']
    list_filter = ['genre', 'category', 'language']

    def user_student_id(self, obj):
        return obj.user.student_id if obj.user else ''
    user_student_id.short_description = 'User Student ID'

admin.site.register(Books, BooksAdmin)