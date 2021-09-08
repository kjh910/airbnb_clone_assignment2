from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument("--total", help="Total making users")
        
    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        seeder.add_entity(User, total, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} users created!"))