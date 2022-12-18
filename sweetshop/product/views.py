from django.core.paginator import Paginator
from django.http import Http404, request
from django.shortcuts import render, get_list_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from sweetshop.product.models import ProductType, Product



class ProductTypeView(views.ListView):
    model = ProductType
    template_name = 'product/product_types.html'
    paginate_by = 2

class ProductView(views.ListView):
    model = Product
    template_name = 'product/product_types_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.filter(type__pk=self.kwargs['pk'])


class ProductDetailView(views.DetailView):
    model = Product
    template_name = 'product/product_details.html'



