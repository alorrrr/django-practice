from django.urls import path
from .views import (
    BookListView,
    BookDetailView, 
    AuthorListView, 
    UserListView, 
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)
from . import views

urlpatterns = [
    path('', BookListView.as_view(), name="meh-home"),
    path('author/<str:pk>/', AuthorListView.as_view(), name="author-detail"),
    path('user/<str:pk>/', UserListView.as_view(), name="user-books"),
    path('books/new/', BookCreateView.as_view(), name="create-book"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('books/<int:pk>/update', BookUpdateView.as_view(), name="book-update"),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name="book-delete"),
]
