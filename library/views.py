from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader

from .models import User, Book, BorrowBook


def index(request):
    book_list = Book.objects.order_by('-date_added')
    context = {'book_list': book_list}
    return render(request, 'library/index.html', context)


def book_details(request, book_id):
    """:arg request
    :param book_id
     :return all users"""
    book_detail = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/detail.html', {'Book details': book_detail})


def users(request):
    """:arg request
    :return all users"""
    users_list = User.objects.order_by('-date_added')
    context = {'All users list': users_list}
    return render(request, 'library/users.html', context)


def get_user(request, user_id):
    """:arg request
    :param user_id
    :return user info"""

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    # user = get_object_or_404(User, pk=user_id)
    return render(request, 'library/user.html', {'User': user})  # HttpResponse("User info: %s" % user_id)


def search_book_by_name(request, book_name):
    """:arg request
    :param book_name"""
    return HttpResponse("The book search: %s" % book_name)


def search_book_by_id(request, book_id):
    """:arg request
    :param book_id"""
    return HttpResponse("The book search: %s" % book_id)


def request_book(request, book_id):
    """:arg request
    :param book_id"""
    return HttpResponse("Requested book is: %s" % book_id)


def return_book(request, book_id):
    """:arg request
    :param book_id
    :return return book and pay fine (if any)"""
    return HttpResponse("Returned book: %s" % book_id)


def approve_request_book(request, book_id):
    """:arg request
    :param book_id"""
    return HttpResponse("Approved book: %s" % book_id)


def all_books(request, user_id):
    """:arg request
    :param user_id
    :return all books"""
    book_list = Book.objects.order_by('-date_added')
    context = {'List of all the books in the system': book_list}
    return render(request, 'library/books.html', context)


def books_borrowed_by_user(request, user_id):
    """:arg request
     :param user_id
    :return all books borrowed by a given user"""
    return HttpResponse("List all the books borrowed by user: %s" % user_id)


def list_of_borrowed_books(request):
    """:arg request
    :return all books borrowed"""
    return HttpResponse("list of all borrowed books are: ")


def list_of_available_books(request):
    """:arg request
    :return return all available books in the system"""


def borrow(request, book_id):
    borrowed_books = get_object_or_404(BorrowBook, pk= book_id)
    return render(request, 'library/borrow.html', {'Books borrowed': borrowed_books})
