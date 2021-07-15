from django.utils import timezone

from apps.bot.bot_telegram.services.check_profile import check_time_task_box
from apps.bot.models import MetasIncomplete, Profile, Edition


def create_task_box(user_name, metas, metas_pro):
    try:
        edition = Edition.objects.filter(active=True).first()
        profile = Profile.objects.filter(user_name=user_name).first()
        MetasIncomplete.objects.create(user_name=profile, metas=metas,
                                       metas_pro=metas_pro, edition=edition)
        return True
    except:
        return False


def add_task_bot(user_name, metas, metas_pro, user_pk):
    metas_incomplete = MetasIncomplete.objects.get(pk=user_pk)

    edition = Edition.objects.filter(active=True).first()
    if not edition:
        return False
    elif edition.pk == metas_incomplete.edition:
        metas_incomplete = MetasIncomplete.objects.get(pk=user_pk)
        metas_incomplete.metas = metas
        metas_incomplete.metas_pro = metas_pro
        metas_incomplete.edition = edition.pk
        metas_incomplete.save(force_update=True)
        return True
    else:
        return create_task_box(user_name, metas, metas_pro)


def add_metas_task_box(user_name, metas, metas_pro):
    """
    ADD task box
    """
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')
    user = Profile.objects.filter(user_name=user_name).first()
    if user:
        task = MetasIncomplete.objects.filter(user_name=user.pk).first()
    else:
        return False
    if not check_time_task_box():
        return False
    elif not task:
        return create_task_box(user_name, metas, metas_pro)
    else:
        if not current_data == task.updated.strftime('%d/%m/%Y'):
            return add_task_bot(user_name, metas, metas_pro, task.pk)

