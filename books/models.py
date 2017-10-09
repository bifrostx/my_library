from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


def category_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/category/<filename>
    return '{0}/{1}'.format(instance.category.slug, filename)


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.views < 0:
            self.views = 0
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.tag


class Book(models.Model):
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)

    title = models.CharField(max_length=128)
    author = models.CharField(max_length=32)
    publisher = models.CharField(max_length=32, blank=True)
    published_date = models.DateField(null=True)
    short_description = models.TextField(blank=True)
    related_url = models.URLField(blank=True)

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)

    upload = models.FileField(upload_to=category_path, blank=True)
    date_uploaded = models.DateTimeField(editable=False)
    date_modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_uploaded = timezone.now()
        self.date_modified = timezone.now()
        return super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
