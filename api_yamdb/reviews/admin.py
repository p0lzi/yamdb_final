from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """ Класс для управления произведениями в админке. """

    list_display = ('pk', 'name', 'year', 'category', 'get_genres')
    search_fields = ('name',)
    list_filter = ('category', 'year')
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Класс для управления категориями произведений в админке. """

    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """ Класс для управления жанрами произведений в админке. """

    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Класс для управления комментариями в админке. """

    list_display = ('pk', 'review', 'author')
    search_fields = ('author', 'text')
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Класс для управления отзывами в админке. """

    list_display = ('pk', 'title', 'author', 'score')
    list_filter = ('title', 'author', 'score')
    search_fields = ('title', 'author')
    empty_value_display = '-пусто-'
