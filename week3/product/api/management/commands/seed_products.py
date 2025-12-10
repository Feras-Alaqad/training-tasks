from django.core.management.base import BaseCommand
from api.models import Product

class Command(BaseCommand):
    help = "Seed the database with dummy products"

    def handle(self, *args, **kwargs):
        products = [
            {"name": "Laptop", "price": 1500.00},
            {"name": "Smartphone", "price": 800.00},
            {"name": "Headphones", "price": 120.50},
        ]

        for p in products:
            Product.objects.get_or_create(name=p["name"], price=p["price"])

        self.stdout.write(self.style.SUCCESS("Dummy products seeded successfully!"))
