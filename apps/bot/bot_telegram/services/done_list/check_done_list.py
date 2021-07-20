from django.utils import timezone

from apps.bot.models import TaskBox, Edition, Profile, DoneList


def check_done_list_exists(id_user):
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')

    edition = Edition.objects.filter(active=True).last()
    profile = Profile.objects.filter(id_user=id_user).last()
    done_list = DoneList.objects.filter(id_user=profile.pk,
                                        edition=edition.pk).last()

    if not done_list:
        return False

    data_complete = done_list.updated.strftime('%d/%m/%Y')
    if data_complete == current_data:
        return True
    else:
        return False
