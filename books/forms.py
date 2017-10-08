from django import forms
from books.models import Category, Book, Tag


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class BookForm(forms.ModelForm):

    title = forms.CharField(label='Title:', max_length=128,
                            help_text="Please enter the title of the book.")
    author = forms.CharField(label='Author:', max_length=32,
                             help_text="Please enter the author of the book, "
                                       "if there are more than one, "
                                       "plese use comma to seprate.")
    publisher = forms.CharField(label='Publisher:', max_length=32,
                                help_text="Please enter the publisher of the book.",
                                required=False)
    published_date = forms.DateField(label='Published Date:', help_text="Please enter the publish date of the book.",
                                     required=False)
    short_description = forms.Textarea()
    related_url = forms.URLField(label="Related URL",required=False)

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    downloads = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    upload = forms.FileField(help_text="Click to upload the book.", required=False)
    date_uploaded = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    date_modified = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Book
        exclude = ('category', 'tag', 'views', 'likes', 'downloads', 'date_uploaded', 'dated_modified',)


class TagForm(forms.ModelForm):
    tag = forms.CharField(label='Tag:', max_length=32,
                            help_text="Please enter the tag name to add a tag.")

    class Meta:
        model = Tag
        fields = ('tag',)