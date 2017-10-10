# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_library.settings')

import django
django.setup()
from django.utils import timezone
from books.models import Category, Book, Tag


def populate():
    programming_books = [
        {"title": "Official Python Tutorial",
         "author": "Python official",
         "publisher": "Python.org",
         "published_date": timezone.now().date(),
         "short_description": "The official tutorial published online.",
         "related_url": "www.python.com",
         "views": 123,
         "likes": 12,
         "downloads": 45},
        {"title": "Tango with Django",
         "author": "Leif Azzopardi",
         "publisher": "Python.org",
         "published_date": "2017-01-01",
         "short_description": "xxx",
         "related_url": "www.tangowithdjango.com",
         "views": 341,
         "likes": 1234,
         "downloads": 1},
        {"title": "Java",
         "author": "Xin Han",
         "publisher": "Python.org",
         "published_date": "2017-01-01",
         "short_description": "",
         "related_url": "www.java.com",
         "views": 1233,
         "likes": 1040,
         "downloads": 1214},]

    physics_books = [
        {"title": "微分几何与广义相对论",
         "author": "梁灿彬",
         "publisher": "科学出版社出版",
         "published_date": "2017-01-01",
         "short_description": "广义相对论",
         "related_url": "http://www.sinap.ac.cn",
         "views": 223,
         "likes": 32,
         "downloads": 45},
        {"title": "量子力学",
         "author": "曾谨言",
         "publisher": "科学出版社出版",
         "published_date": "2011-01-01",
         "short_description": "",
         "related_url": "",
         "views": 331,
         "likes": 144,
         "downloads": 1234},
        {"title": "电动力学",
         "author": "郭硕鸿",
         "publisher": "科学出版社出版",
         "published_date": "2017-01-01",
         "short_description": "",
         "related_url": "",
         "views": 3313,
         "likes": 104,
         "downloads": 124}, ]

    other_books = [
        {"title": "美国种族简史",
         "author": "托马斯·索威尔",
         "publisher": "科学出版社出版",
         "published_date": "2017-01-01",
         "short_description": "",
         "related_url": "",
         "views": 43,
         "likes": 24,
         "downloads": 43},
        {"title": "世界为何存在",
         "author": "吉姆·霍尔特",
         "publisher": "科学出版社出版",
         "published_date": "2017-01-01",
         "short_description": "",
         "related_url": "",
         "views": 341,
         "likes": 1234,
         "downloads": 1},
        {"title": "和韩欣一起飞",
         "author": "Xin Han",
         "publisher": "科学出版社出版",
         "published_date": "2017-01-01",
         "short_description": "",
         "related_url": "",
         "views": 1233,
         "likes": 1040,
         "downloads": 1214}, ]

    cats = {"Programming": {"views": 22, "likes": 12, "books": programming_books},
            "Physics": {"views": 32, "likes": 16, "books": physics_books},
            "Others": {"views": 16, "likes": 8, "books": other_books},}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        if cat_data["books"]:
            for b in cat_data["books"]:
                book = add_book(c, b["title"], b["author"],
                                b['publisher'], b['published_date'],
                                b['short_description'], b['related_url'],
                                b['views'], b['likes'], b['downloads'],)
                add_book_to_tag(book, add_tag("book"))


def add_book(cat, title, author, publisher,
             published_date, short_description,
             related_url, views=0, likes=0, downloads=0, upload=None):
    b = Book.objects.get_or_create(category=cat, title=title)[0]
    b.author = author
    b.publisher = publisher
    b.published_date = published_date
    b.short_description = short_description
    b.upload = upload
    b.related_url = related_url
    b.views = 0
    b.likes = 0
    b.downloads = 0

    b.save()
    return b


def add_book_to_tag(book, tag):
    book.tag.add(tag)
    book.save()


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


def add_tag(tag):
    t = Tag.objects.get_or_create(tag=tag)[0]
    t.save()
    return t

if __name__ == "__main__":
    print("Starting books population script...")
    populate()


