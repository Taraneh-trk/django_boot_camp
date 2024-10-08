from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    fullname = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ForeignKey(Author, related_name='books',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publication_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class LibraryUser(User):
    pass
