from django.urls import path
from .views import BookListView, AuthorListView, UserListView
from . import views

urlpatterns = [
    path('', views.home, name="meh-home"),
    path('author/<str:pk>/', AuthorListView.as_view(), name="author-detail"),
    path('user/<str:pk>/', UserListView.as_view(), name="user-books"), 
    path('books', BookListView.as_view(), name="meh-books"),
]
