from django.shortcuts import render
from .models import Book


def home_page(request):
    return render(request, "library.html")


def add_book(request):
    ...


def delete_book(request):
    ...


def show_books(request):
    books = Book.objects.all()
    return render(request, "show_books.html", context={'books': books})


def search_book_by_name(request):
    ...


def search_book_by_author(request):
    ...


def modify_book(request):
    ...


def filter_book(request):
    ...


def delete_book_by_filter(request):
    ...