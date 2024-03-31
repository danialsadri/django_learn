from random import choice
from accounts.models import User, Profile
from blog.models import Post, Category
from django.core.management.base import BaseCommand
from faker import Faker

category_list = ["IT", "Design", "Fun"]


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.get(email='danielsadri01@gmail.com')
        profile = Profile.objects.get(user=user)

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(5):
            Post.objects.create(
                author=profile,
                category=Category.objects.get(name=choice(category_list)),
                title=self.fake.paragraph(nb_sentences=1),
                content=self.fake.paragraph(nb_sentences=10),
                status=choice([True, False]),
            )
