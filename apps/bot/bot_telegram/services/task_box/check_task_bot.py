from django.utils import timezone

from apps.bot.models import TaskBox, Edition, Profile


def check_task_exists(id_user):
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')

    edition = Edition.objects.filter(active=True).last()
    profile = Profile.objects.filter(id_user=id_user).last()
    task_box = TaskBox.objects.filter(id_user=profile.pk,
                                      edition=edition.pk).last()
    if not task_box:
        return False

    data_incomplete = task_box.updated.strftime('%d/%m/%Y')
    if data_incomplete == current_data:
        return True
    else:
        return False
