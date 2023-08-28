from django.urls import path

from .views import *

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('books/', BooksView.as_view(), name='books'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('book/<slug:book_slug>/', BookView.as_view(), name='book'),
    path('book/<slug:book_slug>/update_book/',
         UpdateBookView.as_view(), name='update_book'),
    path('book/<slug:book_slug>/delete_book/',
         DeleteBookView.as_view(), name='delete_book'),
]
