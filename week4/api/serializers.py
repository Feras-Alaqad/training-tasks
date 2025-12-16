from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

    def validate_name(self, value):
        product_id = self.instance.id if self.instance else None
        if Product.objects.exclude(id=product_id).filter(name=value).exists():
            raise serializers.ValidationError("Product name must be unique.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value
