# serializers.py
from rest_framework import serializers
from .models import Supplier, ProductSupplier, Product, Category

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id',
            'name',
            'email',
            'created_at'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'created_at'
        ]

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category'
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'category_id',
            'created_at'
        ]

class ProductSupplierSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(),
        source='supplier'
    )

    class Meta:
        model = ProductSupplier
        fields = [
            'id',
            'product_id',
            'supplier_id',
            'cost_price',
            'lead_time_days',
            'created_at'
        ]

    def validate(self, data):
        product = data['product']
        supplier = data['supplier']

        if ProductSupplier.objects.filter(
            product=product,
            supplier=supplier
        ).exists():
            raise serializers.ValidationError(
                "This product is already associated with this supplier."
            )

        return data
