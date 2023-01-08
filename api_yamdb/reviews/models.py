import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from django.db import models

from users.models import User

# Константа для проверки года
YEAR_CHOICES = [(y, y) for y in range(datetime.date.today().year + 1)]


class BaseModel(models.Model):
    """ Общая модель для категорий и жанров произведений. """

    name = models.CharField('Название', max_length=256)
    slug = models.SlugField('URL', unique=True, max_length=50,
                            validators=[
                                RegexValidator(regex='[-a-zA-Z0-9_]+')])

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(BaseModel):
    """ Модель категорий для произведений. """

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(BaseModel):
    """ Модель жанров для произведений. """

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Title(models.Model):
    """ Модель произведений. """

    name = models.CharField('Название', max_length=100)
    year = models.IntegerField('Год выпуска', choices=YEAR_CHOICES)
    description = models.TextField('Описание', blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        verbose_name='Жанры'
    )

    class Meta:
        ordering = ('year',)
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def get_genres(self):
        """ Метод возвращает жанры произведения. """

        return ', '.join([obj for obj in self.genre.all()])

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """ Связующая модель для жанров и произведений. """

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'


class Review(models.Model):
    """ Модель отзывов пользователей к произведениям. """

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Текст отзыва'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    score = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        verbose_name='Оценка от 1 до 10'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата отзыва'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_author_title'
            )
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    """ Модель комментариев пользователей к отзывам. """

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Текст нового комментария'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
