from rest_framework.viewsets import ModelViewSet
from .models import Supplier, Category, Product, ProductSupplier
from .serializers import (
    SupplierSerializer,
    CategorySerializer,
    ProductSerializer,
    ProductSupplierSerializer
)

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSupplierViewSet(ModelViewSet):
    queryset = ProductSupplier.objects.all()
    serializer_class = ProductSupplierSerializer
