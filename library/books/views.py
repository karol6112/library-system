from django.shortcuts import render
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, generics
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .serializers import AuthorSerializer, CategorySerializer, BookSerializer, AddOrderSerializer, OrderSerializer
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

    @action(detail=True)
    def borrow(self, request, **kwargs):
        book = self.get_object()
        user = self.request.user

        orders = Order.objects.filter(user=user).filter(book=book)

        if len(orders):
            raise APIException("You have already borrowed this book!")
        else:
            order = Order()
            order.book = book
            order.user = user
            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data)


# class AddOrderView(generics.CreateAPIView):
#     serializer_class = AddOrderSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     # def get_queryset(self):
#     #     user = self.request.user
#     #     orders = Order.objects.filter(user=user)
#     #     return orders
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         book = self.request.data['book']
#         orders = Order.objects.filter(user=user).filter(book=book)
#
#         if len(orders):
#             raise APIException("You have already borrowed this book !")
#
#         else:
#             serializer.save(user=user)
#
#
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            orders = Order.objects.all()
        else:
            orders = Order.objects.filter(user=user)
        return orders

    @action(detail=True)
    def back(self, request, **kwargs):
        order = self.get_object()
        order.active = False
        order.date_end = datetime.datetime.now()
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data)
