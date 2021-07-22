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

        level = Level.objects.all()
        x = 0.1

        for _ in level:
            if x >= _.points <= x:
                print(_.title)
                break
