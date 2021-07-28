from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.bot.models import Level, Ranking


class Command(BaseCommand):
    help = 'comando de teste'

    def handle(self, *args, **kwargs):
        x = 0
        ranking = Ranking.objects.filter(id_user=1)

        for _ in ranking:
            x = x + _.points

        level = Level.objects.all().order_by("number")

        points = 100
        for _ in level:
            if points >= _.points:
                print(f"{_.title}")
                # Nvl 2. Centurião   (+10)