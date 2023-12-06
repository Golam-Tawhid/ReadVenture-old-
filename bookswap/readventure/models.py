from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
import uuid

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
        # Add the book to the user's wishlist
        user.wishlist.add(book)
        
class User(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=20, unique=True, primary_key=True)
    first_name = models.CharField(max_length=30, default='N/A')
    last_name = models.CharField(max_length=30, default='N/A')
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15, default='N/A')
    admin= models.BooleanField(default=False)
    regular= models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    booklist = models.ManyToManyField('Books', related_name='user_books')
    wishlist= models.ManyToManyField('Books', related_name='user_wishlist')
   
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

    
    ratings = models.ManyToManyField('Receipt', related_name='books_ratings')
    reviews = models.ManyToManyField('Receipt', related_name='books_reviews')
    receipt_numbers = models.ManyToManyField('Receipt', related_name='books_receipt_numbers')

    def request_to_borrow(self, borrower):
        Receipt.objects.create(book=self, borrower=borrower)

    def __str__(self):
        return self.title
    
class Receipt(models.Model):
    receipt_no = models.AutoField(primary_key=True, editable=False, unique=True)
    book = models.OneToOneField(Books, on_delete=models.CASCADE)
    borrower = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review = models.TextField(blank=True, max_length=255)  
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.receipt_no)

class Availability(models.Model):
    book = models.OneToOneField(Books, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=30, default='Available')

    def __str__(self):
        return f'{self.book.title} - {self.status}'

class Borrows(models.Model):
    student = models.ManyToManyField(User)
    book = models.ManyToManyField(Books)

    def __str__(self):
        return f'{self.student} - {self.book}'


class Lends(models.Model):
    student = models.ManyToManyField(User)
    book = models.ManyToManyField(Books)

    def __str__(self):
        return f'{self.student} - {self.book}'

##prev
# class Supply(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplied_books', to_field='student_id')
#     borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books', to_field='student_id')

#     def __str__(self):
#         return f'{self.owner} supplies to {self.borrower}'

#GPT
class Supply(models.Model):
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplied_books', to_field='student_id')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books', to_field='student_id')

    def __str__(self):
        return f'{self.supplier} supplies to {self.borrower}'
    
# models.py

# class Wishlist(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
#     book = models.ForeignKey(Books, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('student', 'book')

