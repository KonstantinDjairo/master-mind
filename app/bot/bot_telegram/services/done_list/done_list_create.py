from app.bot.bot_telegram.services.done_list.add_ranking import add_ranking
from app.bot.models import MetasCompleted, Edition


def create_done_list_true(user_name, streak, metas, metas_pro):

    try:
        edition = Edition.objects.filter(active=True).first()
        MetasCompleted.objects.create(user_name=user_name, metas=metas,
                                      metas_pro=metas_pro, streak=streak,
                                      streak_count=1, streak_max=1,
                                      edition=edition)
        return add_ranking(user_name)
    except:
        return False


def create_done_list_false(user_name, streak, metas, metas_pro):

    try:
        edition = Edition.objects.filter(active=True).first()
        MetasCompleted.objects.create(user_name=user_name, metas=metas,
                                      metas_pro=metas_pro, streak=streak,
                                      streak_count=0, streak_max=0,
                                      edition=edition)
        return add_ranking(user_name)
    except:
        return False