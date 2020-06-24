from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet, CategoryViewSet, BookViewSet, OrderViewSet

app_name = 'books'

router = routers.DefaultRouter()
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('orders/', OrderViewSet.as_view(), name='order'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
