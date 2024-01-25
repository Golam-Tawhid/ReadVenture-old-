from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
import uuid
from PIL import Image

class UserManager(BaseUserManager):
    def create_user(self, student_id, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(student_id=student_id, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, student_id, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(student_id, email, password, **extra_fields)
    
    def add_to_wishlist(self, user, book):
        user.wishlist.add(book)
        
class User(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=20, unique=True, primary_key=True)
    first_name = models.CharField(max_length=30, default='N/A')
    last_name = models.CharField(max_length=30, default='N/A')
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15, unique=True,  default='N/A')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    wishlist= models.ManyToManyField('Books', related_name='user_wishlist')

    admin= models.BooleanField(default=False)
    regular= models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'contact_no']

    def __str__(self):
        return self.student_id
    
class Books(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, to_field='student_id')
    title = models.CharField(max_length=100, default='N/A')
    author = models.CharField(max_length=30, default='N/A')
    isbn = models.CharField(max_length=20, default='N/A')
    genre = models.CharField(max_length=30, default='N/A')
    category = models.CharField(max_length=30, default='N/A')
    cover_photo = models.ImageField(upload_to='images/', default='images/default.jpg')
    language = models.CharField(max_length=30, default='N/A')
    condition = models.CharField(max_length=30, default='N/A')
    status = models.CharField(max_length=30, default='Available')

    
    ratings = models.ManyToManyField('Exchange_info', related_name='books_ratings')
    reviews = models.ManyToManyField('Exchange_info', related_name='books_reviews')
    exchange_ids = models.ManyToManyField('Exchange_info', related_name='books_receipt_numbers')
    

    # def request_to_borrow(self, borrower):
    #     Exchange_info.objects.create(book=self, borrower=borrower)

    def __str__(self):
        return self.title
    
class Exchange_info(models.Model):
    exchange_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, to_field='book_id')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, to_field='student_id')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, to_field='student_id', related_name='borrower')
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, default='Pending')


    
# resizing images
# def save(self, *args, **kwargs):
#     super(Supply, self).save(*args, **kwargs)

#     img = Image.open(self.avatar.path)

#     if img.height > 100 or img.width > 100:
#         new_img = (100, 100)
#         img.thumbnail(new_img)
#         img.save(self.avatar.path)