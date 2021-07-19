from django.utils import timezone

from apps.bot.bot_telegram.services.profile.check_profile import check_metas
from apps.bot.bot_telegram.services.ranking.add_ranking import ranking_conf
from apps.bot.bot_telegram.services.done_list.done_list_create import \
    create_done_list_true, create_done_list_false
from apps.bot.models import DoneList, Profile, TaskBox, Edition


def add_done_list(metas_user, streak, metas, metas_pro, metas_ok, id_user):
    done_list = DoneList.objects.get(pk=metas_user.pk)
    edition = Edition.objects.filter(active=True).first()

    if not edition:
        return False

    if metas_ok:
        done_list.metas = metas_user.metas + metas
        done_list.metas_pro = metas_user.metas_pro + metas_pro
        done_list.streak_count += 1
        done_list.streak = streak
        done_list.streak_max += 1
        done_list.edition = edition
        done_list.save()
        return ranking_conf(id_user)
    else:
        done_list.metas = metas_user.metas + metas
        done_list.metas_pro = metas_user.metas_pro + metas_pro
        done_list.streak_count = 0
        done_list.streak = False
        done_list.edition = edition.pk
        done_list.save()
        return ranking_conf(id_user)


def add_metas_done_list(id_user, streak, metas, metas_pro):
    """
    ADD DOTLIST
    """
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')

    profile = Profile.objects.filter(id_user=id_user).first()
    done_list = DoneList.objects.filter(id_user=profile.pk).last()

    task_box_exists = TaskBox.objects.filter(id_user=profile.pk).last()
    date_task_box = task_box_exists.updated.strftime('%d/%m/%Y')

    if not done_list:
        if check_metas(task_box_exists, metas, metas_pro):
            return create_done_list_true(id_user, streak, metas, metas_pro)
        else:
            return create_done_list_false(id_user, streak, metas, metas_pro)
    else:
        metas_user_data = done_list.updated.strftime('%d/%m/%Y')
        if not current_data == metas_user_data and metas_user_data == date_task_box:

            metas_ok = check_metas(task_box_exists, metas, metas_pro)
            return add_done_list(done_list, streak, metas, metas_pro,
                                 metas_ok, id_user)
        else:
            return False


def add_metas_completed(id_user, streak, metas, metas_pro):
    """
    ADD DOTLIST
    """
    return add_metas_done_list(id_user, streak, metas, metas_pro)
