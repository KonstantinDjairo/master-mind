from django.utils import timezone

from apps.bot.bot_telegram.services.profile.check_profile import \
    check_time_task_box
from apps.bot.models import TaskBox, Profile, Edition


def create_task_box(id_user, metas, metas_pro):
    try:
        edition = Edition.objects.filter(active=True).last()
        profile = Profile.objects.filter(id_user=id_user).last()
        TaskBox.objects.create(id_user=profile, metas=metas,
                               metas_pro=metas_pro, edition=edition)
        return True
    except ValueError as e:
        print(f"Erro create_task_box: {e}")
        return False


def add_task_box(id_user, metas, metas_pro, user_pk):
    task_box = TaskBox.objects.filter(pk=user_pk).last()
    edition = Edition.objects.filter(active=True).last()

    if edition.pk == task_box.edition:
        try:
            task_box = TaskBox.objects.get(pk=user_pk)
            task_box.metas = metas
            task_box.metas_pro = metas_pro
            task_box.edition = edition.pk
            task_box.save()
            return True
        except ValueError as e:
            print(f"Erro add_task_box: {e}")
            return False
    else:
        return create_task_box(id_user, metas, metas_pro)


def add_metas_task_box(id_user, metas, metas_pro):
    """
    ADD task box
    """
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')
    profile = Profile.objects.filter(id_user=id_user).last()
    edition = Edition.objects.filter(active=True).last()
    task_box = TaskBox.objects.filter(id_user=profile.pk, edition=edition.pk).last()

    if not task_box:
        return create_task_box(id_user, metas, metas_pro)
    else:
        if not current_data == task.updated.strftime('%d/%m/%Y'):
            return add_task_box(id_user, metas, metas_pro, task.pk)
