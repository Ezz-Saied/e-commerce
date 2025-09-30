from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ListProductView.as_view(), name='product-list'),
    path("product/<slug:slug>", views.ProductDetailView.as_view(),
          name="product-detail"),
]
