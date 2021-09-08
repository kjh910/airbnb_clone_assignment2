from django.urls import path
from books import views as books_view

urlpatterns = [
    path('', books_view.BooksView.as_view(), name='books'),
]
