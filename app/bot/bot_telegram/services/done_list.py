from django.utils import timezone

from app.bot.bot_telegram.services.check_profile import check_metas
from app.bot.models import MetasCompleted, Profile, MetasIncomplete


def add_metas(metas_exists, user_name, streak, metas, metas_x, metas_pro, metas_pro_x):
    """
    ADD DOTLIST
    """
    current_data = timezone.now()
    streak_count = 0

    user = Profile.objects.filter(user_name=user_name).first()
    metas_user = MetasCompleted.objects.filter(user_name=user.pk).first()
    metas_ok = check_metas(metas_exists, metas, metas_pro)

    if not metas_user:
        if metas_ok:
            MetasCompleted.objects.create(user_name=user, metas=metas,
                                          metas_pro=metas_pro, streak=streak,
                                          streak_count=streak_count + 1,
                                          streak_max=1)
            return True
        else:
            MetasCompleted.objects.create(user_name=user, metas=metas,
                                          metas_pro=metas_pro, streak=streak,
                                          streak_count=0, streak_max=0)
            return True
    else:
        if not current_data.strftime('%d/%m/%Y') == metas_user.updated.strftime('%d/%m/%Y'):
            metas_completed = MetasCompleted.objects.get(pk=metas_user.pk)
            # repetição de codigo, eu sei
            if metas_ok:
                metas_completed.metas = metas_user.metas + metas
                metas_completed.metas_pro = metas_user.metas_pro + metas_pro
                metas_completed.streak_count += 1
                metas_completed.streak = streak
                metas_completed.streak_max += 1
                metas_completed.save()
            else:
                metas_completed.metas = metas_user.metas + metas
                metas_completed.metas_pro = metas_user.metas_pro + metas_pro
                metas_completed.streak_count = 0
                metas_completed.streak = False
                metas_completed.save()
            return True
        else:
            return False


def add_metas_completed(user_name, streak, metas, metas_x, metas_pro, metas_pro_x):
    """
    ADD DOTLIST
    """
    user = Profile.objects.filter(user_name=user_name).first()
    metas_exists = MetasIncomplete.objects.filter(user_name=user.pk)

    if metas_exists:
        status_ok = add_metas(metas_exists, user_name, streak, metas,
                              metas_x, metas_pro, metas_pro_x)
        if status_ok:
            return True
        else:
            return False
    else:
        return False
