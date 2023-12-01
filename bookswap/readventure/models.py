from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, student_id, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(student_id=student_id, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=20, unique=True, primary_key=True)
    first_name = models.CharField(max_length=30, default='N/A')
    last_name = models.CharField(max_length=30, default='N/A')
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15, default='N/A')
    admin= models.BooleanField(default=False)
    regular= models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'contact_no']

    def __str__(self):
        return self.student_id
    
class Books(models.Model):
    title = models.CharField(max_length=100, default='N/A')
    author = models.CharField(max_length=30, default='N/A')
    isbn = models.CharField(max_length=20, unique=True, default='N/A')
    genre = models.CharField(max_length=30, default='N/A')
    category = models.CharField(max_length=30, default='N/A')
    cover_photo = models.ImageField(upload_to='images/', default='images/default.jpg')
    book_id = models.CharField(max_length=20, unique=True, default='N/A', primary_key=True)
    owner_id = models.CharField(max_length=20, default='N/A')
    language = models.CharField(max_length=30, default='N/A')
    condition = models.CharField(max_length=30, default='N/A')
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='student_id', related_name='books')

    def __str__(self):
        return self.title
    
class Receipt(models.Model):
    recept_no = models.CharField(max_length=20, unique=True, default='N/A')
    book_id = models.CharField(max_length=20, default='N/A')
    borrower_id = models.CharField(max_length=20, default='N/A')
    due_date = models.DateField(auto_now=False, auto_now_add=False, default='N/A')
    return_date = models.DateField(auto_now=False, auto_now_add=False, default='N/A')
    
