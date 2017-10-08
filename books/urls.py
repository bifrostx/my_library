from django.conf.urls import url, include
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^categories/$', views.category_list, name='category_list'),
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)$', views.show_category, name='show_category'),
    url(r'^book/(?P<id>[\d]+)$', views.show_book, name='show_book'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_book/$', views.add_book, name='add_book'),
]