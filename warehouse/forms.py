'''forms'''
from django import forms
from .views import Book

class BookForm(forms.ModelForm):
    '''adding book'''
    title = forms.CharField(label='Tytuł', max_length=150)
    authors = forms.CharField(label='Autorzy', max_length=100)
    publishedDate = forms.IntegerField(label='Data publikacji')
    categories = forms.CharField(label='Kategoria', max_length=200)
    description = forms.CharField(label='Opis', max_length=500)
    class Meta:
        model = Book
        fields = '__all__'
        