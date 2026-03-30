import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Cria ou atualiza um superusuario a partir de variaveis de ambiente.'

    def handle(self, *args, **options):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not username or not email or not password:
            self.stdout.write(
                self.style.WARNING(
                    'Superusuario ignorado: defina DJANGO_SUPERUSER_USERNAME, '
                    'DJANGO_SUPERUSER_EMAIL e DJANGO_SUPERUSER_PASSWORD.'
                )
            )
            return

        user_model = get_user_model()

        if not hasattr(user_model, 'USERNAME_FIELD'):
            raise CommandError('O modelo de usuario atual nao possui USERNAME_FIELD.')

        user, created = user_model.objects.get_or_create(
            **{user_model.USERNAME_FIELD: username},
            defaults={
                'email': email,
                'is_staff': True,
                'is_superuser': True,
            },
        )

        changed = created

        if user.email != email:
            user.email = email
            changed = True
        if not user.is_staff:
            user.is_staff = True
            changed = True
        if not user.is_superuser:
            user.is_superuser = True
            changed = True
        if not user.check_password(password):
            user.set_password(password)
            changed = True

        if changed:
            user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" criado com sucesso.'))
            return

        if changed:
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" atualizado com sucesso.'))
            return

        self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" ja estava configurado.'))
