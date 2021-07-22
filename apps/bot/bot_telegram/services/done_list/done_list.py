from django.utils import timezone

from apps.bot.bot_telegram.services.profile.check_profile import check_metas
from apps.bot.bot_telegram.services.ranking.add_ranking import ranking_conf
from apps.bot.bot_telegram.services.done_list.done_list_create import \
    create_done_list_true, create_done_list_false
from apps.bot.bot_telegram.services.done_list.bonos import add_bonus
from apps.bot.models import DoneList, Profile, TaskBox, Edition


def add_done_list_false(id_user, done_list, edition, metas, metas_pro):
    try:
        done_list.metas = done_list.metas + metas
        done_list.metas_pro = done_list.metas_pro + metas_pro
        done_list.streak_count = 0
        done_list.streak = False
        done_list.edition = edition
        done_list.save()
        return ranking_conf(id_user, metas, metas_pro)
    except ValueError as e:
        print(f"Erro add_done_list_false: {e}")
        return False


def add_done_list_true(id_user, done_list, edition, metas, metas_pro):
    try:
        done_list.metas = done_list.metas + metas
        done_list.metas_pro = done_list.metas_pro + metas_pro
        done_list.streak_count += 1
        done_list.streak = True
        done_list.streak_max += 1
        done_list.edition = edition
        done_list.save()
        return ranking_conf(id_user, metas, metas_pro)
    except ValueError as e:
        print(f"Erro add_done_list_false: {e}")
        return False


def add_metas_done_list(id_user, streak, metas, metas_pro):
    """
     add_metas_done_list
    """
    edition = Edition.objects.filter(active=True).last()
    profile = Profile.objects.filter(id_user=id_user).last()
    task_box_exists = TaskBox.objects.filter(id_user=profile.pk).last()
    done_list = DoneList.objects.filter(id_user=profile.pk,
                                        edition=edition).last()

    # Esta meio feio de entender mas funciona
    if not done_list:
        if check_metas(task_box_exists, metas, metas_pro):
            # pela regra de negocio o streak_count reset a casa edição
            return create_done_list_true(id_user, streak, metas, metas_pro,
                                         edition, profile)
        else:
            return create_done_list_false(id_user, streak, metas, metas_pro,
                                          edition, profile)
    else:
        if check_metas(task_box_exists, metas, metas_pro):
            if add_done_list_true(id_user, done_list, edition, metas, metas_pro):
                return add_bonus(profile, edition)
            else:
                return False
        else:
            return add_done_list_false(id_user, done_list, edition, metas, metas_pro)
