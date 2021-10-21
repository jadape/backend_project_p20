
from django.contrib                                import admin
from django.urls                                   import path
from authAppExample.views.brandView import BrandDetailView
from rest_framework_simplejwt.views                import (TokenObtainPairView, TokenRefreshView)
from authAppExample                                import views

urlpatterns = [
    path('admin/',   admin.site.urls),
    path('login/',   TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/',    views.UserCreateView.as_view()),
    
    path('product/',                 views.ProductCreateView.as_view()),
    path('product/<int:pk>/',        views.ProductDetailView.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view()),
    path('brand/create/',            views.BrandCreateView.as_view()),
    path('brand/update/<int:pk>/',   views.BrandUpdateView.as_view()),
    path('brand/delete/<int:pk>/',   views.BrandDeleteView.as_view()),
    path('brand/<int:pk>/',          views.BrandDetailView.as_view())
]
