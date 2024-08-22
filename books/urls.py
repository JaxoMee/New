from django.urls import path
from .views import BooksListAPIView,BookDetailAPIView,BookDeleteAPIView,BookUpdateAPIView,BookCreateAPIView,BookListCreateAPIView

urlpatterns = [
    path('api/v1/books/', BooksListAPIView.as_view()),
    path('api/v1/book/<int:pk>/', BookDetailAPIView.as_view()),
    path('api/v1/book/delete/<int:pk>/', BookDeleteAPIView.as_view()),
    path('api/v1/book/update/<int:pk>/', BookUpdateAPIView.as_view()),
    path("api/v1/book/create/", BookCreateAPIView.as_view()),
    path("api/v1/book/listcreate/",BookListCreateAPIView.as_view()),
]