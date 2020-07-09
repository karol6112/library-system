import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, generics
from rest_framework.decorators import action
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

    @action(detail=True)
    def borrow(self, request, **kwargs):
        book = self.get_object()
        user = self.request.user
        orders = book.order_book.filter(active=True)
        # orders = Order.objects.filter(book=book).filter(active=True)

        if len(orders) == book.amount:
            raise APIException("This book in not available")

        user_orders = orders.filter(user=user)

        if len(user_orders):
            raise APIException("You have already borrowed this book!")
        else:
            order = Order()
            order.book = book
            order.user = user
            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data)


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
