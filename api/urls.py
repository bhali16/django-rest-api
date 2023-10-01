from django.urls import path
from api.views import get_books, book, add_book

urlpatterns = [
    path('', get_books, name="get-books"),
    path('<int:pk>',book, name='book'),
    path('add', add_book, name="add-book"),
]
