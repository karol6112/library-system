from rest_framework import serializers
from .models import Author, Category, Book, Order


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'nick',
            'first_name',
            'last_name',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'category_name',
        )


class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    # author = AuthorSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'category',
            'author',
            'year',
            'isbn',
            'amount',
        )


class AddOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'book',
        )


class OrderSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'book',
            'user',
            'date_start',
            'date_end',
            'active',
        )

