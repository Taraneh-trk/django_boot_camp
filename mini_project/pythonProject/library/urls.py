
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('show_books/', views.show_books, name='show_books'),
]
