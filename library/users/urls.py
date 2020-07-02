from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterUserView, UserView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', obtain_jwt_token, name='login'),
    path('me/', UserView.as_view(), name='me'),
    path('<slug:pk>/', UserProfileView.as_view(), name='profile'),
]
