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

    def __str__(self):
        return self.title
    
class Receipt(models.Model):
    receipt_no = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    borrower = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review = models.TextField(blank=True,max_length=100)
    due_date = models.DateField(default='N/A')
    return_date = models.DateField(default='N/A')

    def __str__(self):
        return str(self.receipt_no)

class Wishlist(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, to_field='student_id')
    wishlist = models.CharField(max_length=30, default='N/A')

    class Meta:
        unique_together = ('student', 'wishlist')

    def __str__(self):
        return f'{self.student} - {self.wishlist}'

class Booklist(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, to_field='student_id')
    booklist = models.CharField(max_length=30, default='N/A')

    class Meta:
        unique_together = ('student', 'booklist')

    def __str__(self):
        return f'{self.student} - {self.booklist}'

# class Author(models.Model):
#     author = models.CharField(max_length=30, default='N/A')
#     book= models.ForeignKey(Books, on_delete=models.CASCADE, to_field='book_id',related_name='authors')

#     class Meta:
#         unique_together = ('author', 'book')

#     def __str__(self):
#         return f'{self.author} - {self.book}'


# class Availability(models.Model):
#     book = models.OneToOneField(Books, on_delete=models.CASCADE, primary_key=True)
#     status = models.CharField(max_length=30, default='Available')

#     def __str__(self):
#         return f'{self.book.title} - {self.status}'

# class Borrows(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE, to_field='student_id')
#     book = models.ForeignKey(Books, on_delete=models.CASCADE, to_field='book_id')

#     class Meta:
#         unique_together = ('student', 'book')

#     def __str__(self):
#         return f'{self.student} - {self.book}'


# class Lends(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE, to_field='student_id')
#     book = models.ForeignKey(Books, on_delete=models.CASCADE, to_field='book_id')

#     class Meta:
#         unique_together = ('student', 'book')

#     def __str__(self):
#         return f'{self.student} - {self.book}'

# class Reviews(models.Model):
  
#     book = models.OneToOneField(Books, on_delete=models.CASCADE, primary_key=True, unique=True)
#     review = models.OneToOneField(Receipt, on_delete=models.CASCADE, to_field='review', unique=True, max_length=255)


#     def __str__(self):
#         return f'{self.book} - {self.review}'


# class Ratings(models.Model):
#     book = models.OneToOneField(Books, on_delete=models.CASCADE, primary_key=True, unique=True)
#     rating = models.OneToOneField(Receipt, on_delete=models.CASCADE, to_field='rating', unique=True)

#     def __str__(self):
#         return f'{self.book} - {self.rating}'

# class Receipt_num(models.Model):
#     book = models.OneToOneField(Books, on_delete=models.CASCADE, primary_key=True, related_name='receipt_numbers')
#     receiptno = models.OneToOneField(Receipt, on_delete=models.CASCADE, to_field='receipt_no', unique=True)

#     def __str__(self):
#         return f'{self.book} - {self.receiptno}'

# class Supply(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplied_books', to_field='student_id')
#     borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books', to_field='student_id')

#     def __str__(self):
#         return f'{self.owner} supplies to {self.borrower}'