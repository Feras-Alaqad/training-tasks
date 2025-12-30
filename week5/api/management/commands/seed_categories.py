from django.core.management.base import BaseCommand
from api.models import Category

class Command(BaseCommand):
    help = "Seed categories table"

    def handle(self, *args, **kwargs):
        categories = [
            "Electronics",
            "Fashion",
            "Home",
            "Sports",
            "Books",
        ]

        for name in categories:
            Category.objects.get_or_create(name=name)

        self.stdout.write(self.style.SUCCESS("Categories seeded successfully"))
