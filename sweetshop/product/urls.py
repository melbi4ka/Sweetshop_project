from django.urls import path

from sweetshop.product.views import ProductView, ProductTypeView, ProductDetailView

urlpatterns = (
    path("type/", ProductTypeView.as_view(), name="product type"),
    path("type/<int:pk>/", ProductView.as_view(), name="product type list"),
    path("type/<int:pk>/<slug:slug>/", ProductDetailView.as_view(), name="product details"),
)