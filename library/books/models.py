import datetime

from django.db import models
from users.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Author(models.Model):
    nick = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        if self.nick:
            return f'{self.first_name} {self.last_name}' + f' ({self.nick})'
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    YEAR = [(r, r) for r in range(datetime.datetime.now().year, 1850, -1)]

    title = models.CharField(max_length=100, blank=False)
    author = models.ManyToManyField(Author)  # some books have more than one authors
    year = models.IntegerField(choices=YEAR, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    amount = models.IntegerField(default=1)
    category = models.ForeignKey(Category, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    date_start = models.DateTimeField(auto_now=True)
    date_end = models.DateTimeField(default=None, blank=-True, null=True)
    active = models.BooleanField(default=True, auto_created=True)