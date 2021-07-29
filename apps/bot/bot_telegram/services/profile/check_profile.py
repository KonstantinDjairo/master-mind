from django.utils import timezone

from apps.bot.models import Profile


def check_profile_exists(id_user):
    profile_exists = Profile.objects.filter(id_user=id_user).last()
    if profile_exists:
        return True
    else:
        return False


def check_time_task_box():
    time_str = timezone.now()
    time = int(time_str.strftime("%H"))
    # horario maximo para mandar a task bot
    if time > 11:
        return True
    else:
        return False


def check_metas(metas_exists, metas, metas_pro):
    if metas_exists.metas == metas and metas_exists.metas_pro == metas_pro:
        return True
    else:
        return False


def check_profile_active(id_user):
    profile = Profile.objects.filter(id_user=id_user).last()
    if profile.active:
        return True
    else:
        return False


def chek_profile(id_user):
    profile = check_profile_exists(id_user).last()
    if profile:
        return True
    else:
        return False
