from django.core.management.base import BaseCommand
from app.bot.main_bot import main
import datetime
from django.utils import timezone
import datetime


class Command(BaseCommand):
    # comando start bot
    help = 'hora'

    def handle(self, *args, **kwargs):
        nowDj = timezone.now()
        #now = datetime.datetime.now()
        now = datetime.date.today()
      
        print(f"normal: {now.strftime('%d/%m/%Y')}")
        print(f"dango: {nowDj.strftime('%d/%m/%Y')}")
        
        print(f"hora djando: {nowDj.strftime('%H')}")
        hora =  int(nowDj.strftime('%H'))
        hora = 1
        if hora < 10:
            print("ok")
        else:
            print("nao")
