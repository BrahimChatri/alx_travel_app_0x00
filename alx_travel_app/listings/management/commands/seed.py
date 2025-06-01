from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create users
        for _ in range(5):
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )

        users = User.objects.all()

        # Create listings
        for _ in range(20):
            Listing.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                price_per_night=round(random.uniform(50, 500), 2),
                location=fake.city(),
                owner=random.choice(users)
            )

        self.stdout.write(self.style.SUCCESS('✅ Database seeded.'))
