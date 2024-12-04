from django.shortcuts import render
from django.http import HttpResponse

books_list = [
    {
        'author': 'Haruki Murakami',
        'title': 'Hear the Wind Sing',
        'year': '1979',
        'about': 'First part of the Rat Thrilogy'
    },
    {
        'author': 'Haruki Murakami',
        'title': 'Pinball, 1973',
        'year': '1980',
        'about': 'Second part of the Rat Thrilogy'
    },
    {
        'author': 'Haruki Murakami',
        'title': 'A Wild Sheep Chase',
        'year': '1982',
        'about': 'Third part of the Rat Thrilogy'
    },
    {
        'author': 'Haruki Murakami',
        'title': 'Dance, Dance, Dance',
        'year': '1994',
        'about': 'Ending part of the Rat Thrilogy'
    }
]

# Create your views here.
def home(request):
    return render(request, 'meh/home.html')

def books(request):
    context = {
        'books': books_list
    }
    return render(request, 'meh/books.html', context)