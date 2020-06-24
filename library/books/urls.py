from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet, CategoryViewSet

app_name = 'books'

router = routers.DefaultRouter()
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
