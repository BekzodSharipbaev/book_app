from django.contrib import admin

from .models import *

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'date_published',
                    'rating',)
    list_display_links = ('title', 'author', )
    list_filter = ('rating', 'view_count',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'slug',)
    list_display_links = ('name', 'surname',)
    search_fields = ('name', 'surname',)
    prepopulated_fields = {'slug': ('name', 'surname',)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
