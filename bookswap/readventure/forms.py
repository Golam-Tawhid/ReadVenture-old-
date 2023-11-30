from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Books

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'student_id', 'email', 'contact_no', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        for fieldname in ['first_name', 'last_name', 'student_id', 'email', 'contact_no']:
            self.fields[fieldname].widget.attrs['placeholder'] = fieldname.replace('_', ' ').capitalize()


class Addbooksform(forms.ModelForm):
    class Meta:
        model= Books
        fields =  ['title', 'author', 'isbn', 'genre', 'category','language','cover_image'] 
        #'cover_image', 'book_id','owner_id','language','condition']

    def save(self, user, commit=True):
        instance = super().save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance