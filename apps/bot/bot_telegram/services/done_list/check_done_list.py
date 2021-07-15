from django.utils import timezone

from apps.bot.models import MetasIncomplete, Edition, Profile, MetasCompleted


def check_done_list_exists(user_name):
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')

    edition = Edition.objects.filter(active=True).last()
    if not edition:
        return False

    user_name = Profile.objects.filter(user_name=user_name).first()

    metas_incomplete = MetasIncomplete.objects.filter(user_name=user_name.pk,
                                                      edition=edition.pk).last()
    metas_complete = MetasCompleted.objects.filter(user_name=user_name.pk,
                                                   edition=edition.pk).last()
    if not metas_incomplete:

        return False
    if not metas_complete:
        return False

    data_complete = metas_complete.updated.strftime('%d/%m/%Y')
    print(data_complete + " - " + current_data)
    if data_complete == current_data:
        return True
    else:
        return False