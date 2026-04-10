# serializers.py
import os

from PIL.Image import Image
from rest_framework import serializers
from .models import Supplier, ProductSupplier, Product, Category
from django.contrib.auth.models import User

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password2"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user

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
    image_url = serializers.SerializerMethodField()
    image = serializers.ImageField(required=False)
    
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
            'image',
            'image_url',
            'deleted_at',
            'created_at'
        ]
        read_only_fields = ['created_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            url = obj.image.url
            return request.build_absolute_uri(url) if request else url
        return None   


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image']

    def validate_image(self, image):
        from PIL import Image
        import os

        if image.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image must be < 2MB")

        ext = os.path.splitext(image.name)[1].lower()
        if ext not in [".jpg", ".jpeg", ".png", ".webp"]:
            raise serializers.ValidationError("Invalid format")

        try:
            img = Image.open(image)
            img.verify()
        except Exception:
            raise serializers.ValidationError("Not a valid image")

        return image
    
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

