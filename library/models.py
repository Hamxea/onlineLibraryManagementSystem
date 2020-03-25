from django.db import models

# Create your models here.
from library.enums import enums


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.IntegerField(choices=enums.GenderEnum.choices())

    def __str__(self):
        return "%s" % self.username


class Book(models.Model):
    book_title = models.CharField(max_length=450)
    category_id = models.IntegerField(choices=enums.BookCategoryEnum.choices())
    author = models.CharField(max_length=150)
    book_copies = models.IntegerField(default=1)
    book_pub = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=150)
    isbn = models.CharField(max_length=100)
    copyright_year = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.IntegerField(choices=enums.BookStatusEnum.choices(), default=enums.BookStatusEnum.ACTIVE)

    def __str__(self):
        return "%s %s %s %s %s" % (self.book_title, self.author, self.book_pub, self.publisher_name, self.isbn)


class BorrowBook(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True, blank=True)
    due_date = models.DateTimeField(auto_now_add=True, blank=True)


class ReturnBook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    return_date = models.DateTimeField(auto_now_add=True, blank=True)


class LostBook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_lost = models.DateTimeField(auto_now_add=True, blank=True)
