from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import User


def index(request):
    return HttpResponse("Welcome to LMS")


def users(request):
    """:arg request
    :return all users"""
    return HttpResponse("All users")


def get_user(request, user_id):
    """:arg request
    :param user_id
    :return user info"""

    """
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    """
    user = get_object_or_404(User, pk=user_id)
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


def all_books(request):
    """:arg request
    :return all books"""
    return HttpResponse("List of all the books in the system")


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


def borrow(request, user_id, book_id):
    return HttpResponse("The book detail borrowed is: %s %s" % user_id, book_id)
