from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


from .models import Supplier, Category, Product, ProductSupplier
from .serializers import (
    ProductImageSerializer,
    SupplierSerializer,
    CategorySerializer,
    ProductSerializer,
    ProductSupplierSerializer
)
from rest_framework import status
from .serializers import SignupSerializer
from .filters import ProductFilter
from rest_framework.decorators import action
import os
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignupSerializer


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "User created successfully",
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()

    
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_class = ProductFilter
    search_fields = ["name"]
    ordering_fields = ["created_at", "price", "name"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return (
            Product.objects
            .filter(
                user=self.request.user,
                deleted_at__isnull=True
            )
            .select_related("category", "user")
            .prefetch_related("product_suppliers__supplier")
            .distinct()
        )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            return Response({
                "message": "No products found matching your search/filter",
                "data": []
            })
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()

        if product.deleted_at:
            return Response({"message": "Product already in trash"})

        product.soft_delete() 

        return Response({"message": "Product moved to trash"})

    @action(detail=False, methods=['get'])
    def trash(self, request):
        products = Product.objects.filter(
            user=request.user,
            deleted_at__isnull=False
        ).select_related("category", "user").prefetch_related("product_suppliers__supplier")

        if not products.exists():
            return Response({
                "message": "Trash is empty",
                "data": []
            })
    
        data = []
        for p in products:
            data.append({
                "id": p.id,
                "name": p.name,
                "category": p.category.name,
                "supplier": [ps.supplier.name for ps in p.product_suppliers.all()],
                "owner": p.user.username,
                "deleted_at": p.deleted_at
            })

        return Response(data)
    @action(detail=True, methods=['post'])
    def restore(self, request, pk=None):
        try:
            product = Product.all_objects.get(pk=pk, user=request.user)

        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found or does not belong to you"},
                status=status.HTTP_404_NOT_FOUND
            )

        product.deleted_at = None
        product.save()

        return Response({"message": "Product restored successfully"})
    
    @action(detail=True, methods=['delete'])
    def force_delete(self, request, pk=None):
        try:
            product = Product.all_objects.get(pk=pk, user=request.user)

        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found or does not belong to you"},
                status=status.HTTP_404_NOT_FOUND
            )

        product.delete()

        return Response({"message": "Product permanently deleted"})
    
    @action(detail=True, methods=['patch'], url_path='update-image')
    def update_image(self, request, pk=None):
        product = self.get_object()

        serializer = ProductImageSerializer(
            product,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Image updated successfully",
                "image_url": product.image.url if product.image else None
            })

        return Response(serializer.errors, status=400)

class ProductSupplierViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSupplierSerializer
    permission_classes = [IsAuthenticated]
    queryset = ProductSupplier.objects.all()

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

