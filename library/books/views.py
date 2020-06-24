from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, generics
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .serializers import AuthorSerializer, CategorySerializer, BookSerializer, OrderSerializer
from .models import Author, Category, Book, Order
from .permissions import IsAdminOrReadOnly


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['nick']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category', 'author']
    filterset_fields = ['category', 'year', 'author']
    ordering_fields = '__all__'


class OrderViewSet(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     orders = Order.objects.filter(user=user)
    #     return orders

    def perform_create(self, serializer):
        user = self.request.user
        book = self.request.data['book']
        orders = Order.objects.filter(user=user).filter(book=book)

        if len(orders):
            raise APIException("You have already borrowed this book !")

        else:
            serializer.save(user=user)

