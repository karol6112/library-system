"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

API_TITLE = "Library system"
API_DESCRIPTION = """This app allow to manage library. It consist of two parts. The first part is "User" app where we can register and log in to account. we also can update our profile. The second is "book" app where we can add book to our library. Each book is assigned to the author and category. The application can filter and search data. In this part are also two functions "borrow" and "back" which allow to borrow book and return it."""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/books/', include('books.urls')),
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
