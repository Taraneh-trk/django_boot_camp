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


class AddBookFormJustTitle(forms.Form):
    title = forms.CharField(max_length=200)


class AddBookFormJustAuthor(forms.Form):
    fullname = forms.CharField(max_length=200)


class ModifyForm(forms.Form):
    title_find_base_on = forms.CharField(max_length=200)
    title = forms.CharField(max_length=200)
    authors = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    publication_date = forms.DateField()
    description = forms.CharField(max_length=200)


class FilterForm(forms.Form):
    min_price = forms.DecimalField()
    max_price = forms.DecimalField()
    start_date = forms.DateField()
    end_date = forms.DateField()