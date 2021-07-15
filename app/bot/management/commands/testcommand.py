from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'comando'

    def handle(self, *args, **kwargs):
        print("funcionando")
