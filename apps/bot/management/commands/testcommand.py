from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):

    help = 'comando'

    def handle(self, *args, **kwargs):
        time_str = timezone.now()
        time = time_str.strftime("%H:%M")
        print(time)

