"""authProjectExample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib                                import admin
from django.urls                                   import path
from authAppExample.views.brandView import BrandDetailView
from rest_framework_simplejwt.views                import (TokenObtainPairView, TokenRefreshView)
from authAppExample                                import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',   TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/',    views.UserCreateView.as_view()),
    path('user/<int:pk>/',    views.UserDetailView.as_view()),
    
    path('product/',                 views.ProductCreateView.as_view()),
    path('product/<int:pk>/',        views.ProductDetailView.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view()),
    path('brand/create/',            views.BrandCreateView.as_view()),
    path('brand/update/<int:pk>/',   views.BrandUpdateView.as_view()),
    path('brand/delete/<int:pk>/',   views.BrandDeleteView.as_view()),
    path('brand/<int:pk>/',      views.BrandDetailView.as_view())
]
