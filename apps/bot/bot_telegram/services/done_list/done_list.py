from django.utils import timezone

from apps.bot.bot_telegram.services.profile.check_profile import check_metas
from apps.bot.bot_telegram.services.ranking.add_ranking import ranking_conf
from apps.bot.bot_telegram.services.done_list.done_list_create import \
    create_done_list_true, create_done_list_false
from apps.bot.models import DoneList, Profile, TaskBox, Edition


def add_create_done_list(streak, metas, metas_pro, metas_ok, id_user):

    try:
        edition = Edition.objects.filter(active=True).last()
        profile = Profile.objects.filter(id_user=id_user).last()
        if metas_ok:
            DoneList.objects.create(id_user=profile, metas=metas,
                                    metas_pro=metas_pro, streak=streak,
                                    streak_count=1, streak_max=1,
                                    edition=edition)
        else:
            DoneList.objects.create(id_user=profile, metas=metas,
                                    metas_pro=metas_pro, streak=streak,
                                    streak_count=0,streak_max=0,
                                    edition=edition)
        return ranking_conf(id_user, metas, metas_pro)
    except ValueError as e:
        print(f"Erro add_create_done_list: {e}")
        return False


def add_done_list(metas_user, streak, metas, metas_pro, metas_ok, id_user):
    done_list = DoneList.objects.get(pk=metas_user.pk)
    edition = Edition.objects.filter(active=True).last()

    if edition.pk == done_list.edition:
        if metas_ok:
            done_list.metas = metas_user.metas + metas
            done_list.metas_pro = metas_user.metas_pro + metas_pro
            done_list.streak_count += 1
            done_list.streak = streak
            done_list.streak_max += 1
            done_list.edition = edition
            done_list.save()
        else:
            done_list.metas = metas_user.metas + metas
            done_list.metas_pro = metas_user.metas_pro + metas_pro
            done_list.streak_count = 0
            done_list.streak = False
            done_list.edition = edition
            done_list.save()
    else:
        pass
    return ranking_conf(id_user, metas, metas_pro)


def add_metas_done_list(id_user, streak, metas, metas_pro):
    """
     add_metas_done_list
    """
    profile = Profile.objects.filter(id_user=id_user).last()
    done_list = DoneList.objects.filter(id_user=profile.pk).last()
    task_box_exists = TaskBox.objects.filter(id_user=profile.pk).last()

    if not done_list:
        if check_metas(task_box_exists, metas, metas_pro):
            return create_done_list_true(id_user, streak, metas, metas_pro)
        else:
            return create_done_list_false(id_user, streak, metas, metas_pro)
    else:
        metas_ok = check_metas(task_box_exists, metas, metas_pro)
        return add_done_list(done_list, streak, metas, metas_pro, metas_ok, id_user)





