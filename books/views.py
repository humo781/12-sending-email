from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .mixins import BookMixin
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "book/book_list.html"
    context_object_name = "books"

class BookDetailView(BookMixin, DetailView):
    template_name = 'book/book_detail.html'


class BookCreateView(BookMixin, CreateView):
    template_name = 'book/add_book.html'
    fields = ('title', 'description', 'author_name', 'published_at')

    def get_success_url(self):
        return reverse_lazy('list')

class BookUpdateView(BookMixin, UpdateView):
    template_name = 'book/add_book.html'
    fields = ('title', 'description', 'author_name', 'published_at')

    def get_success_url(self):
        return reverse_lazy('list')

class BookDeleteView(BookMixin, DeleteView):
    template_name = 'book/confirm.html'

    def get_success_url(self):
        return reverse_lazy('list')
