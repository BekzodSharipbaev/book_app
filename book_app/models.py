from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    title = models.CharField(max_length=255, verbose_name='Название книги')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    author = models.ForeignKey(
        'Author', on_delete=models.PROTECT, verbose_name='Автор')
    date_published = models.DateField(verbose_name='Год издания')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр')
    rating = models.IntegerField(choices=RATING_CHOICES)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):
        return reverse("book", kwargs={"book_slug": self.slug})

    def update_url(self):
        return reverse("update_book", kwargs={"book_slug": self.slug})

    def delete_url(self):
        return reverse("delete_book", kwargs={"book_slug": self.slug})

    def increment_view_count(self):
        self.view_count = models.F('view_count') + 1
        self.save()
        self.refresh_from_db(fields=['view_count', ])

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя автора')
    surname = models.CharField(max_length=255, verbose_name='Фамилия автора')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name} - {self.surname}'

    def get_absolute_url(self):
        return reverse('author', kwargs={'author_slug': self.slug})

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название жанра')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_slug': self.slug})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
