from django.utils import timezone

from app.bot.bot_telegram.services.check_profile import check_metas
from app.bot.bot_telegram.services.done_list.add_ranking import add_ranking
from app.bot.bot_telegram.services.done_list.done_list_create import \
    create_done_list_true, create_done_list_false
from app.bot.models import MetasCompleted, Profile, MetasIncomplete, Edition


def add_done_list(metas_user, streak, metas, metas_pro, metas_ok, user_name):
    metas_completed = MetasCompleted.objects.get(pk=metas_user.pk)
    edition = Edition.objects.filter(active=True).first()

    if not edition:
        return False

    if metas_ok:
        metas_completed.metas = metas_user.metas + metas
        metas_completed.metas_pro = metas_user.metas_pro + metas_pro
        metas_completed.streak_count += 1
        metas_completed.streak = streak
        metas_completed.streak_max += 1
        metas_completed.edition = edition.pk
        metas_completed.save()
        return add_ranking(user_name)
    else:
        metas_completed.metas = metas_user.metas + metas
        metas_completed.metas_pro = metas_user.metas_pro + metas_pro
        metas_completed.streak_count = 0
        metas_completed.streak = False
        metas_completed.edition = edition.pk
        metas_completed.save()
        return add_ranking(user_name)


def add_metas_done_list(metas_exists, user_name, streak, metas, metas_pro):
    """
    ADD DOTLIST
    """
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')
    user = Profile.objects.filter(user_name=user_name).first()
    metas_user = MetasCompleted.objects.filter(user_name=user.pk).first()
    metas_user_data = metas_user.updated.strftime('%d/%m/%Y')

    if not metas_user:
        if check_metas(metas_exists, metas, metas_pro):
            return create_done_list_true(user_name, streak, metas, metas_pro)
        else:
            return create_done_list_false(user_name, streak, metas, metas_pro)
    else:
        if not current_data == metas_user_data:
            metas_ok = check_metas(metas_exists, metas, metas_pro)
            return add_done_list(metas_user, streak, metas, metas_pro,
                                 metas_ok,user_name)
        else:
            return False


def add_metas_completed(user_name, streak, metas, metas_pro):
    """
    ADD DOTLIST
    """
    user = Profile.objects.filter(user_name=user_name).first()
    metas_exists = MetasIncomplete.objects.filter(user_name=user.pk)

    if metas_exists:
        return add_metas_done_list(metas_exists, user_name, streak, metas,
                                   metas_pro)
    else:
        return False
