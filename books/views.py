# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Category, Book, Tag
from .forms import CategoryForm, BookForm, TagForm


def index(request):
    most_download_books = Book.objects.order_by('-downloads')[:5]
    most_liked_books = Book.objects.order_by('-likes')[:5]
    categories = Category.objects.all()

    return render(request, 'books/index.html',
                  {"most_download_books": most_download_books,
                   "most_liked_books": most_liked_books,
                   "categories": categories})


def about(request):
    return render(request, 'books/about.html')


def category_list(request):
    cats = Category.objects.all().order_by('name')
    return render(request, 'books/category_list.html', {"category_list": cats})


def book_list(request):
    books = Book.objects.all().order_by('pk')
    return render(request, 'books/book_list.html', {"book_list": books})


def show_category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    books = Book.objects.filter(category=category)
    return render(request, 'books/show_category.html', {'category': category, 'books': books})


def edit_book(request, id):
    book = Book.objects.get(pk=id)
    tags = Tag.objects.filter(book=book)
    try:
        form = BookForm(
            {"title": book.title,
             "author": book.author,
             "publisher": book.publisher,
             "published_date": book.published_date,
             "short_description": book.short_description,
             "related_url": book.related_url,
             "views": book.views,
             "likes": book.likes,
             "downloads": book.downloads,
             "upload": book.upload,
             "date_uploaded": book.date_uploaded,
             "date_modified": book.date_modified}
        )
    except form.DoesNotExist:
        return index(request)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'books/show_book.html', {'book': book, 'tags': tags})
        else:
            print(form.errors)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book, 'tags': tags})


def show_book(request, id):
    book = Book.objects.get(pk=id)
    tags = Tag.objects.filter(book=book)
    return render(request, 'books/show_book.html', {'book': book, 'tags': tags})


def add_tag(request, id):
    book = Book.objects.get(pk=id)
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=True)
            book.tag.add(tag)
    return redirect('books:show_book', book.id)


def add_book(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            if category:
                book = form.save(commit=False)
                book.category = category
                form.save(commit=True)
                tag = Tag.objects.get_or_create(tag=category.slug)[0]
                book.tag.add(tag)
                form.save(commit=True)
                return redirect('books:show_category', category_name_slug)
        else:
            print(form.errors)

    return render(request, 'books/add_book.html', {'form': form})


def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'books/add_category.html', {'form': form})


def download(request, id):
    book = Book.objects.get(pk=id)
    book.downloads += 1
    book.save()
    return redirect('books:serve', book.upload)


def like_book(request):

    book_id = None
    if request.method == 'GET':
        book_id = request.GET['book_id']

    likes = 0
    if book_id:
        book = Book.objects.get(id=int(book_id))

        if book:
            likes = book.likes + 1
            book.likes = likes
            book.save()

    return HttpResponse(likes)


def search(request):
    results = []
    if request.method == 'GET':
        input = request.GET['query']
        query_list = input.split()
        for query in query_list:
            outputs = Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(short_description__icontains=query) |
                Q(tag__tag__icontains=query)
            )
            for output in outputs:
                results.append(output)
    results = set(results)
    return render(request, 'books/search_results.html', {'results': results, 'query': input})

