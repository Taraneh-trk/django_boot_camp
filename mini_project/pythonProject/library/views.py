from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import AddBookForm, AddAuthorForm, AddBookFormTitle
from django.urls import reverse


def home_page(request):
    return render(request, "library.html")


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            Book.objects.create(
                title=form.cleaned_data['title'],
                authors=Author.objects.get(fullname=form.cleaned_data['authors']),
                price=form.cleaned_data['price'],
                publication_date=form.cleaned_data['publication_date'],
                description=form.cleaned_data['description'],
            )
            return redirect(reverse('home_page'))
    else:
        form = AddBookForm()
    return render(request, 'add_book_form.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(
                fullname=form.cleaned_data['fullname'],
            )
            return redirect(reverse('home_page'))
    else:
        form = AddAuthorForm()
    return render(request, 'add_author_form.html', {'form': form})


def delete_book(request):
    if request.method == 'POST':
        form = AddBookFormTitle(request.POST)
        if form.is_valid():
            book = Book.objects.filter(
                title=form.cleaned_data['title'],
                authors=(Author.objects.get(fullname=form.cleaned_data['authors'])).id,
            )
            book.delete()
            return redirect(reverse('home_page'))
    else:
        form = AddBookFormTitle()
    return render(request, 'delete_book_form.html', {'form': form})


def show_books(request):
    books = Book.objects.all()
    return render(request, "show_books.html", context={'books': books})


def search_book_by_name(request):
    ...


def search_book_by_author(request):
    ...


def modify_book(request):
    ...


def filter_book_by_price(request):
    ordered_book = Book.objects.order_by('price')
    return render(request, "ordered_book.html", context={'ordered_book': ordered_book})


def filter_book_by_date(request):
    ordered_book = Book.objects.order_by('publication_date')
    return render(request, "filter_book_by_date.html", context={'ordered_book': ordered_book})


def delete_book_by_filter(request):
    ...