from django.core.management.base import BaseCommand
from django_seed import Seed

from people.models import Person
class Command(BaseCommand):
        
    def handle(self, *args, **options):
        people = [
            "Actor",
            "Director",
            "Writer"
        ]
        for a in people:
            Person.objects.create(name=a,kind=a)
        self.stdout.write(self.style.SUCCESS(" people created!"))