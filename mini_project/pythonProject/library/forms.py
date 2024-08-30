from django import forms


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=200)
    authors = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    publication_date = forms.DateField()
    description = forms.CharField(max_length=200)


class AddAuthorForm(forms.Form):
    fullname = forms.CharField(max_length=200)


class AddBookFormTitle(forms.Form):
    title = forms.CharField(max_length=200)
    authors = forms.CharField(max_length=200)

