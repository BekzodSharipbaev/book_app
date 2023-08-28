from django import forms

from .models import *


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'slug', 'author',
                  'date_published', 'genre', 'rating', ]
        
