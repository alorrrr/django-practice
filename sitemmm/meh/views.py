from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def home(request):
    return render(request, 'meh/home.html')

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'meh/books.html', context)