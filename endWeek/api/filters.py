import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    category_id = django_filters.NumberFilter(field_name="category_id")
    supplier_id = django_filters.NumberFilter(
        field_name="product_suppliers__supplier_id"
    )
    price = django_filters.NumberFilter(field_name="price")
    price__gte = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price__lte = django_filters.NumberFilter(field_name="price", lookup_expr="lte")


    class Meta:
        model = Product
        fields = ["category_id", "supplier_id", "price", "price__gte", "price__lte"]
