from django.core.management.base import BaseCommand
from django_seed import Seed

from categories.models import Category
class Command(BaseCommand):
        
    def handle(self, *args, **options):
        categories = [
            "Book",
            "Movie",
            "Both"
        ]
        for a in categories:
            Category.objects.create(name=a,kind=a)
        self.stdout.write(self.style.SUCCESS(" Categories created!"))