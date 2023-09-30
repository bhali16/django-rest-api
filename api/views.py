from django.shortcuts import render
from api.models import Book
from django.http import JsonResponse

def book_list(request):
    books = Book.objects.all()
    bookPython = list(books.values())
    return JsonResponse({
        'books': bookPython
    })
