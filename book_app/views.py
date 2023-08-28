from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import *

# Create your views here.

menu_titles = [{'title': 'Главная страница', 'url_name': 'start_page'},
               {'title': 'Книги', 'url_name': 'books'},
               {'title': 'Добавление книги', 'url_name': 'add_book'},
               {'title': 'О книге', 'url_name': 'book'},
               {'title': 'Обновление книги', 'url_name': 'update_book'},
               {'title': 'Удаление книги', 'url_name': 'delete_book'},
               ]


class StartPageView(TemplateView):
    template_name = 'book_app/start_page.html'
    extra_context = {'title': 'Главная страница', 'menu_titles': menu_titles}


class BooksView(ListView):
    model = Book
    template_name = 'book_app/books.html'
    context_object_name = 'books'
    extra_context = {'title': 'Книги', 'menu_titles': menu_titles}


class AddBookView(CreateView):
    form_class = AddBookForm
    template_name = 'book_app/add_book.html'
    success_url = reverse_lazy('books')
    extra_context = {'title': 'Добавление книги', 'menu_titles': menu_titles}


class BookView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book_app/book.html'
    slug_url_kwarg = 'book_slug'
    extra_context = {'title': 'О книге', 'menu_titles': menu_titles}

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.increment_view_count()
        return obj


class UpdateBookView(UpdateView):
    model = Book
    form_class = AddBookForm
    template_name = 'book_app/update_book.html'
    slug_url_kwarg = 'book_slug'
    extra_context = {'title': 'Обновление книги', 'menu_titles': menu_titles}


class DeleteBookView(DeleteView):
    model = Book
    template_name = 'book_app/delete_book.html'
    slug_url_kwarg = 'book_slug'
    success_url = reverse_lazy('books')
    extra_context = {'title': 'Удаление книги', 'menu_titles': menu_titles}
