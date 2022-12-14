from django.contrib import admin

from sweetshop.product.models import ProductType, Product


# Register your models here.
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('type', '-id')
    list_display = ('id', 'type', "name")
    list_filter = ('type', "name")
    search_fields = ('id', "name", 'description')
    sortable_by = ('type', 'name')
    list_per_page = 5

