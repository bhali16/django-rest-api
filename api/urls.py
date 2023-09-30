from django.urls import path
from api.views import book_list

urlpatterns = [
    path('list', book_list, name="booklist")
]
