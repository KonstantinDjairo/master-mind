from django.utils import timezone

from app.bot.bot_telegram.check_profile import check_time_task_box
from app.bot.models import MetasIncomplete, Profile


def add_metas_incomplete(user_name, metas, metas_pro):
    """
    ADD task box
    """
    current_data = timezone.now()

    user = Profile.objects.filter(user_name=user_name).first()
    user_metas = MetasIncomplete.objects.filter(user_name=user.pk).first()
    status_ok = check_time_task_box()

    if not status_ok:
        return False
    elif not user_metas:
        MetasIncomplete.objects.create(user_name=user, metas=metas,
                                       metas_pro=metas_pro)
        return True
    else:
        if not current_data.strftime('%d/%m/%Y') == user_metas.updated.strftime('%d/%m/%Y'):
            metas_incomplete = MetasIncomplete.objects.get(pk=user_metas.pk)
            metas_incomplete.metas = metas
            metas_incomplete.metas_pro = metas_pro
            metas_incomplete.save(force_update=True)
            return True
        else:
            return False