
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('show_books/', views.show_books, name='show_books'),
    path('filter_book_by_price/', views.filter_book_by_price, name='filter_book_by_price'),
    path('filter_book_by_date/', views.filter_book_by_date, name='filter_book_by_date'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('search_book_by_name/', views.search_book_by_name, name='search_book_by_name'),
    path('search_book_by_author/', views.search_book_by_author, name='search_book_by_author'),
    path('modify_book/', views.modify_book, name='modify_book'),
    path('modify_book/', views.modify_book, name='modify_book'),
    path('filter_by_date_price/', views.filter_by_date_price, name='filter_by_date_price'),
    path('delete_book_by_filter/', views.delete_book_by_filter, name='delete_book_by_filter'),
]
