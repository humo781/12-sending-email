from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Book

class BookMixin(LoginRequiredMixin):
    model = Book
    login_url = reverse_lazy('login')
