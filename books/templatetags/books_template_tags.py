from django import template
from books.models import Category, Book

register = template.Library()


@register.inclusion_tag('books/get_counts.html')
def get_counts():

    book_num = Book.objects.all().count()

    if book_num is None:
        book_num = 0

    return {'book_num': book_num}