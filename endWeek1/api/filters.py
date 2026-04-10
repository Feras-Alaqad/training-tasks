import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    category_id = django_filters.NumberFilter(field_name="category_id")
    supplier_id = django_filters.NumberFilter(
        field_name="product_suppliers__supplier_id"
    )

    class Meta:
        model = Product
        fields = ["category_id", "supplier_id"]
