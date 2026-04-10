# serializers.py
from rest_framework import serializers
from .models import Supplier, ProductSupplier, Product, Category

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email', 'created_at']
        read_only_fields = ['created_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['created_at']

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'category_id',
            'category_name',
            'created_at'
        ]
        read_only_fields = ['created_at']


class ProductSupplierSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(),
        source='supplier',
        write_only=True
    )

    product_name = serializers.ReadOnlyField(source='product.name')
    supplier_name = serializers.ReadOnlyField(source='supplier.name')

    class Meta:
        model = ProductSupplier
        fields = [
            'id',
            'product_id',
            'supplier_id',
            'product_name',
            'supplier_name',
            'cost_price',
            'lead_time_days',
            'created_at'
        ]
        read_only_fields = ['created_at']

