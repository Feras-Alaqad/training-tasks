from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Supplier, Category, Product, ProductSupplier
from .serializers import (
    SupplierSerializer,
    CategorySerializer,
    ProductSerializer,
    ProductSupplierSerializer
)
class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Supplier.objects.all()
    
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()

from .filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_class = ProductFilter

    search_fields = [
        "name",
    ]

    ordering_fields = [
        "created_at",
        "price",
        "name"
    ]

    ordering = ["-created_at"] 

    def get_queryset(self):
        return (
            Product.objects
            .filter(user=self.request.user)
            .select_related("category", "user")
            .prefetch_related("product_suppliers__supplier")
            .distinct()
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class ProductSupplierViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSupplierSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            ProductSupplier.objects
            .filter(product__user=self.request.user)
            .select_related("product", "supplier")
        )

class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        products = Product.objects.filter(user=request.user)

        latest_products = (
            products
            .select_related("category", "user")
            .prefetch_related("product_suppliers__supplier")
            .order_by("-created_at")[:5]
        )

        data = {
            "total_products": products.count(),
            "total_categories": Category.objects.count(),
            "total_suppliers": Supplier.objects.count(),
            "latest_products": ProductSerializer(latest_products, many=True).data
        }

        return Response({
            "success": True,
            "data": data
        })
