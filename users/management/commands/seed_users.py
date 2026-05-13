from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed default test users (manager, staff, resident) for the dispatch system'

    def handle(self, *args, **options):
        User = get_user_model()

        users = [
            {'username': 'admin', 'password': 'admin1234', 'role': 'manager', 'is_superuser': True},
            {'username': 'manager1', 'password': 'Test1234!', 'role': 'manager'},
            {'username': 'staff1', 'password': 'Test1234!', 'role': 'staff'},
            {'username': 'staff2', 'password': 'Test1234!', 'role': 'staff'},
            {'username': 'resident1', 'password': 'Test1234!', 'role': 'resident'},
            {'username': 'resident2', 'password': 'Test1234!', 'role': 'resident'},
        ]

        for u in users:
            username = u['username']
            if User.objects.filter(username=username).exists():
                self.stdout.write(f'Already exists: {username}')
                continue

            user = User.objects.create_user(
                username=username,
                password=u['password'],
            )
            user.role = u['role']
            if u.get('is_superuser'):
                user.is_staff = True
                user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created: {username} (role={u["role"]})'))

        self.stdout.write(self.style.SUCCESS('User seeding complete.'))
