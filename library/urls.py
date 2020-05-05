from os import name

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.borrow, name='borrow'),

]

"""
path('<int:user_id>/books', views.all_books, name='all_books'),
path('<int:user_id>/users/', views.users, name='users')
"""