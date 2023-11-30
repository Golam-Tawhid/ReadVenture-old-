from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    # Add the additional fields
    first_name = models.CharField(max_length=30, default='N/A')
    last_name = models.CharField(max_length=30, default='N/A')
    student_id = models.CharField(max_length=20, unique=True, default='N/A')
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15, default='N/A')
    
    # username = models.CharField(max_length=30, unique=True, default='N/A')
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'student_id'
    # REQUIRED_FIELDS = ['first_name', 'last_name', 'student_id', 'email', 'contact_no']

    def __str__(self):
        return self.student_id
    
class Books(models.Model):
    # Add the additional fields
    title = models.CharField(max_length=100, default='N/A')
    author = models.CharField(max_length=30, default='N/A')
    isbn = models.CharField(max_length=20, unique=True, default='N/A')
    genre = models.CharField(max_length=30, default='N/A')
    category = models.CharField(max_length=30, default='N/A')
    cover_photo = models.ImageField(upload_to='images/', default='images/default.jpg')
    #book_id = models.CharField(max_length=20, unique=True, default='N/A')
    #owner_id = models.CharField(max_length=20, default='N/A')
    language = models.CharField(max_length=30, default='N/A')
    #conditon = models.CharField(max_length=30, default='N/A')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Receipt(models.Model):
    # Add the additional fields
    recept_no = models.CharField(max_length=20, unique=True, default='N/A')
    book_id = models.CharField(max_length=20, default='N/A')
    borrower_id = models.CharField(max_length=20, default='N/A')
    due_date = models.DateField(auto_now=False, auto_now_add=False, default='N/A')
    return_date = models.DateField(auto_now=False, auto_now_add=False, default='N/A')
    
