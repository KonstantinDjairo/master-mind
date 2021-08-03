from apps.bot.bot_telegram.services.ranking.add_ranking import ranking_conf
from apps.bot.models import DoneList


def create_done_list_true(id_user, streak, metas, metas_pro, edition, profile):
    """
    create done list_true(id_user, streak, metas, metas_pro):

    """
    done_list = DoneList.objects.filter(id_user=profile.pk).last()
    if not done_list:
        streak_max = 0
    else:
        streak_max = done_list.streak_max
    try:
        DoneList.objects.create(id_user=profile, metas=metas,
                                metas_pro=metas_pro, streak=streak,
                                streak_count=1, streak_max=streak_max + 1,
                                edition=edition)
        metas = metas + 1
        return ranking_conf(id_user, metas, metas_pro)
    except Exception as e:
        print(f"Erro create_done_list_true: {e}")
        return False


def create_done_list_false(id_user, streak, metas, metas_pro, edition, profile):
    """
    create_done_list_false
    """
    done_list = DoneList.objects.filter(id_user=profile.pk).last()
    if not done_list:
        streak_max = 0
    else:
        streak_max = done_list.streak_max
    try:
        DoneList.objects.create(id_user=profile, metas=metas,
                                metas_pro=metas_pro, streak=streak,
                                streak_count=0, streak_max=streak_max + 1,
                                edition=edition)
        return ranking_conf(id_user, metas, metas_pro)
    except Exception as e:
        print(f"Erro create_done_list_false: {e}")
        return False
