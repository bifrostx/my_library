from django.shortcuts import render, redirect
from .models import Category, Book, Tag
from .forms import CategoryForm, BookForm, TagForm


def index(request):
    recent_uploaded_books = Book.objects.order_by('-date_uploaded')[:5]
    most_liked_books = Book.objects.order_by('-likes')[:5]
    categories = Category.objects.all()
    return render(request, 'books/index.html',
                  {"recent_uploaded_books": recent_uploaded_books,
                   "most_liked_books": most_liked_books,
                   "categories": categories})


def about(request):
    return render(request, 'books/about.html', {"a": "a"})


def category_list(request):
    cats = Category.objects.all().order_by('name')
    return render(request, 'books/category_list.html', {"category_list": cats})


def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'books/book_list.html', {"book_list": books})


def show_category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    books = Book.objects.filter(category=category)
    return render(request, 'books/show_category.html', {'category': category, 'books': books})


def show_book(request, id):
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
            return render(request, 'books/show_book.html', {'form': form, 'book': book})
        else:
            print(form.errors)
    return render(request, 'books/show_book.html', {'form': form, 'book': book, 'tags': tags})


def add_tag(request, id):
    book = Book.objects.get(pk=id)
    if request.method == "POST":
        print("is post")
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
                return index(request)
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
