import re
from apps.bot.models import Level, DoneList, Ranking, Profile, Edition


def check_level(message, id_user):
    """
        !!!!
        depois eu vou consertar isso, função provisorio
        !!!!
    """
    global metas_pro, start, metas, level_user, number
    points = 0

    profile = Profile.objects.filter(id_user=id_user).last()
    ranking = Ranking.objects.filter(id_user=profile.pk)
    level = Level.objects.all()

    if "ProMode" in message:
        pro_mode = re.search(r"ProMode", message)
        start = pro_mode.start()
        end = len(message)
        message_pro_mode = message[start:end]
        meta_pro_list_incomplete = re.findall("⏱", message_pro_mode)
        metas_pro = len(meta_pro_list_incomplete)

    if "Metas" in message:
        metas_list = re.findall("⏱", message[0:start])
        metas = len(metas_list)

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
