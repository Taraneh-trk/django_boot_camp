from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import AddBookForm, AddAuthorForm, AddBookFormTitle, AddBookFormJustTitle, AddBookFormJustAuthor, ModifyForm, FilterForm
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
    if request.method == 'POST':
        form = AddBookFormJustTitle(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            books = Book.objects.filter(title=title)
            return render(request, 'search_book_by_name.html', {'books': books})
    else:
        form = AddBookFormJustTitle()
    return render(request, 'search_book_by_name_form.html', {'form': form})


def search_book_by_author(request):
    if request.method == 'POST':
        form = AddBookFormJustAuthor(request.POST)
        if form.is_valid():
            author_name = form.cleaned_data['fullname']
            books = Book.objects.filter(authors__fullname=author_name)
            return render(request, 'search_book_by_author.html', {'books': books})
    else:
        form = AddBookFormJustAuthor()

    return render(request, 'search_book_by_author_form.html', {'form': form})


def modify_book(request):
    if request.method == 'POST':
        form = ModifyForm(request.POST)
        if form.is_valid():
            book = Book.objects.filter(title=form.cleaned_data['title_find_base_on'])
            book.update(
                title=form.cleaned_data['title'],
                authors=Author.objects.get(fullname=form.cleaned_data['authors']),
                price=form.cleaned_data['price'],
                publication_date=form.cleaned_data['publication_date'],
                description=form.cleaned_data['description'],
            )
            return redirect(reverse('home_page'))
    else:
        form = ModifyForm()

    return render(request, 'modify_book_form.html', {'form': form})


def filter_book_by_price(request):
    ordered_book = Book.objects.order_by('price')
    return render(request, "ordered_book.html", context={'ordered_book': ordered_book})


def filter_book_by_date(request):
    ordered_book = Book.objects.order_by('publication_date')
    return render(request, "filter_book_by_date.html", context={'ordered_book': ordered_book})


def filter_by_date_price(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            books = Book.objects.filter(
                price__lte=max_price,
                price__gte=min_price,
                publication_date__lte=end_date,
                publication_date__gte=start_date,
            )

            return render(request, 'filter_by_date_price.html', {'books': books})
    else:
        form = FilterForm()

    return render(request, 'filter_by_date_price_form.html', {'form': form})


def delete_book_by_filter(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            books = Book.objects.filter(
                price__lte=max_price,
                price__gte=min_price,
                publication_date__lte=end_date,
                publication_date__gte=start_date,
            )
            books.delete()
            return redirect(reverse('home_page'))
    else:
        form = FilterForm()

    return render(request, 'filter_by_date_price_form.html', {'form': form})
