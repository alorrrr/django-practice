from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Book

def home(request):
    return render(request, 'meh/home.html')

class BookListView(ListView):
    model = Book
    template_name = "meh/books.html"
    context_object_name = 'books'
    ordering = ['-id']

class AuthorListView(ListView):
    model = Book
    template_name = "meh/author_detail.html"
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_url = self.kwargs['pk']
        context['books'] = Book.objects.filter(author_url=author_url)  # Фильтруем книги по author_url
        return context

class UserListView(ListView):
    model = Book
    template_name = "meh/user_books.html"
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['pk']
        context['books'] = Book.objects.filter(username__username=username)  # Фильтруем книги по author_url
        return context

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'meh/books.html', context)