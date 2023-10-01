from django.shortcuts import render
from api.models import Book
from api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)