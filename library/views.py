from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse("Welcome to LMS")


def users(request):
    """:param request
    :return all users"""
    return HttpResponse("All users")


def all_books(request):
    """:param request, books
    :return all books"""
    return HttpResponse("List of all the books in the system")


def books_borrowed_by_user(request, user_id):
    """    :param request, user_id:
    :return all books borrowed by a given user"""
    return HttpResponse("List all the books borrowed by user: %s" % user_id)


def borrow(request, user_id, book_id):
    return HttpResponse("The book detail borrowed is: %s %s" % user_id, book_id)
