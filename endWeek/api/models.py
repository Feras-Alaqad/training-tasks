from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.core.exceptions import ValidationError


class ProductManager(models.Manager):
    def active(self):
        return self.filter(deleted_at__isnull=True)

    def trashed(self):
        return self.filter(deleted_at__isnull=False)
    
class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=255)
    price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(Decimal("0.00"))]
)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True,
        default='products/download.png'
    )

    deleted_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()        
    all_objects = models.Manager()

    def is_deleted(self):
        return self.deleted_at is not None
    
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

        
class ProductSupplier(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_suppliers'
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='product_suppliers'
    )

    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    lead_time_days = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['product', 'supplier']

    def __str__(self):
        return f"{self.product} - {self.supplier}"
