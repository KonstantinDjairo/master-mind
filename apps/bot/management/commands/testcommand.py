from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.bot.models import Level


class Command(BaseCommand):
    help = 'comando de teste'

    def handle(self, *args, **kwargs):

        global level_user
        level = Level.objects.all()
        pontos = 55
        for _ in level:
            if pontos < _.points > pontos:
                print(_.number)
                level_user = _.number
                break

        level_user = level_user - 1

        n = Level.objects.filter(number=level_user).first()

        print(n.points)
