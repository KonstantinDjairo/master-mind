from django.utils import timezone

from ..models import Profile


def check_profile_exists(user_name):
    profile_exists = Profile.objects.filter(user_name=user_name)
    if profile_exists:
        return True
    else:
        return False


def check_time_task_box():
    time_str = timezone.now()
    time = int(time_str.strftime('%H'))

    if time < 10:
        return True
    else:
        return False


def check_metas(metas_exists, metas, metas_pro):
    for dado in metas_exists:
        metas_ = dado.metas
        metas_pro_ = dado.metas_pro

    if metas_ == metas and metas_pro_ == metas_pro:
        return True
    else:
        return False


def check_profile_active(user_name):
    user = Profile.objects.filter(user_name=user_name).first()
    if user.active:
        return True
    else:
        return False


def chek_profile(user_name):
    profile = check_profile_exists(user_name)
    if profile:
        return True
    else:
        return False
