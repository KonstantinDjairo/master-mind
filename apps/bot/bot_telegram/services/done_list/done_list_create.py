from apps.bot.bot_telegram.services.ranking.add_ranking import ranking_conf
from apps.bot.models import MetasCompleted, Edition, Profile


def create_done_list_true(user_name, streak, metas, metas_pro):
    edition = Edition.objects.filter(active=True).first()
    profile = Profile.objects.filter(user_name=user_name).first()

    if not edition or not profile:
        return False

    profile = Profile.objects.filter(user_name=user_name).first()
    MetasCompleted.objects.create(user_name=profile, metas=metas,
                                  metas_pro=metas_pro, streak=streak,
                                  streak_count=1, streak_max=1,
                                  edition=edition)
    return ranking_conf(user_name)


def create_done_list_false(user_name, streak, metas, metas_pro):
    edition = Edition.objects.filter(active=True).first()
    profile = Profile.objects.filter(user_name=user_name).first()
    if not edition or not profile:
        return False

    MetasCompleted.objects.create(user_name=profile, metas=metas,
                                  metas_pro=metas_pro, streak=streak,
                                  streak_count=0, streak_max=0,
                                  edition=edition)
    return ranking_conf(user_name)
