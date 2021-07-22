import re
from apps.bot.models import Level, DoneList, Ranking, Profile, Edition
from apps.bot.bot_telegram.message_filters.filter_task_box import \
    filter_task_box


def check_level(message, id_user):
    """
        !!!!
        depois eu vou consertar isso, função provisorio
        !!!!
    """
    points = 0
    number = 0
    profile = Profile.objects.filter(id_user=id_user).last()
    ranking = Ranking.objects.filter(id_user=profile.pk)
    level = Level.objects.all()

    lista = filter_task_box(message)
    metas = lista[0]["metas"]
    metas_pro = lista[0]["metas_pro"]

    for _ in ranking:
        points += _.points

    for _ in level:
        if points < _.points >= points:
            number = _.number
            break

    level = Level.objects.filter(number=number-1).last()

    if metas > level.metas or metas_pro > level.metas_pro:
        return True
    else:
        return False
