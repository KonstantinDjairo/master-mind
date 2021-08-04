from django.utils import timezone

from apps.bot.bot_telegram.services.profile.check_profile import check_metas
from apps.bot.bot_telegram.services.done_list.done_list_create import \
    create_done_list_true, create_done_list_false
from apps.bot.bot_telegram.services.done_list.bonos import add_bonus
from apps.bot.models import DoneList, Profile, TaskBox, Edition


def add_metas_done_list(id_user, streak, metas, metas_pro):
    """
     add_metas_done_list
    """

    # TENHO QUE OTIMIZAR ESSE CODIGO
    edition = Edition.objects.filter(active=True).last()
    profile = Profile.objects.filter(id_user=id_user).last()
    task_box_exists = TaskBox.objects.filter(id_user=profile.pk).last()

    if check_metas(task_box_exists, metas, metas_pro):
        if create_done_list_true(id_user, streak, metas, metas_pro,
                                 edition, profile):
            return add_bonus(profile)
        else:
            return False
    else:
        return create_done_list_false(id_user, streak, metas, metas_pro,
                                      edition, profile)
