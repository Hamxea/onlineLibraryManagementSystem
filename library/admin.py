from django.contrib import admin

# Register your models here.
from .models import User, Book, BorrowBook, ReturnBook, LostBook

admin.site.register(User)
admin.site.register(Book)
admin.site.register(BorrowBook)
admin.site.register(LostBook)
admin.site.register(ReturnBook)
#admin.site.register(ReturnBook)