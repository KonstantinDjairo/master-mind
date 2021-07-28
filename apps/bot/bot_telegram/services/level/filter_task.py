import re

from apps.bot.models import Level, DoneList, Ranking, Profile, Edition
from apps.bot.bot_telegram.message_filters.filter_task_box import \
    filter_task_box
from .level_up import get_level_to_profile


def check_level(message, id_user):
    """
        Check level so user
    """
    profile = Profile.objects.filter(id_user=id_user).last()
    lista = filter_task_box(message)

    metas = lista[0]["metas"]
    metas_pro = lista[0]["metas_pro"]

    number = get_level_to_profile(profile)
    level = Level.objects.filter(number=number).first()

    if not level.metas >= metas and level.metas_pro >= metas_pro:
        return True
    else:
        return False

