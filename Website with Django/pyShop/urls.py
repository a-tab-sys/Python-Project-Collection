"""pyShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# our pyShop app also has a urls module. this is like the parent urls module in out django project. we need to tell django pyshop app about our products app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))       #any request that starts with products/ should be delegated to products app (our products url module)
]
