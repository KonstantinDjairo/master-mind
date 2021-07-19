from apps.bot.bot_telegram.services.ranking.add_ranking import ranking_conf
from apps.bot.models import DoneList, Edition, Profile


def create_done_list_true(id_user, streak, metas, metas_pro):
    """
    def create_done_list_true(id_user, streak, metas, metas_pro):

    """
    edition = Edition.objects.filter(active=True).last()
    profile = Profile.objects.filter(user_name=id_user).last()

    if not edition or not profile:
        return False
    try:
        profile = Profile.objects.filter(user_name=id_user).last()
        DoneList.objects.create(id_user=profile, metas=metas,
                                metas_pro=metas_pro, streak=streak,
                                streak_count=1, streak_max=1,
                                edition=edition)
    except ValueError as e:
        print(f"Erro create_done_list_true: {e}")
        return False
    return ranking_conf(id_user, metas, metas_pro)


def create_done_list_false(id_user, streak, metas, metas_pro):
    """
    create_done_list_false
    """
    edition = Edition.objects.filter(active=True).first()
    profile = Profile.objects.filter(id_user=id_user).first()

    if not edition or not profile:
        return False
    try:
        DoneList.objects.create(id_user=profile, metas=metas,
                                metas_pro=metas_pro, streak=streak,
                                streak_count=0, streak_max=0,
                                edition=edition)
    except ValueError as e:
        print(f"Erro create_done_list_false: {e}")
        return False
    return ranking_conf(id_user, metas, metas_pro)
