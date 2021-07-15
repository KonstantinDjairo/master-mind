from app.bot.models import MetasIncomplete, Edition, Profile
from django.utils import timezone


def check_task_exists(user_name):
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')

    edition = Edition.objects.filter(active=True).last()
    if not edition:
        return False
    user_name = Profile.objects.filter(user_name=user_name).first()
    metas_incomplete = MetasIncomplete.objects.filter(user_name=user_name.pk,
                                                      edition=edition.pk).last()

    data_incomplete = metas_incomplete.updated.strftime('%d/%m/%Y')
    if data_incomplete == current_data:
        return True
    else:
        return False
