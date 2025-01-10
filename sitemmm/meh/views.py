from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from django.urls import reverse
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "meh/books.html"
    context_object_name = 'books'
    ordering = ['-id']
    paginate_by = 5

    
class BookDetailView(DetailView):
    model = Book

class AuthorListView(ListView):
    model = Book
    template_name = "meh/author_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_url = self.kwargs['pk']
        context['books'] = Book.objects.filter(author_url=author_url).order_by('-id')
        return context

class UserListView(ListView):
    model = Book
    template_name = "meh/user_books.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['pk']
        context['books'] = Book.objects.filter(username__username=username).order_by('-id')
        return context

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'year', 'about']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'year', 'about']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        book = self.get_object()
        if self.request.user == book.username:
            return True
        return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book

    def get_success_url(self):
        book = self.get_object()
        return reverse('user-books', args=[book.username.username])

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.username:
            return True
        return False
    
