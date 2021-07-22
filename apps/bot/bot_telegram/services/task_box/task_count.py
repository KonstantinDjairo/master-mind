from apps.bot.models import TaskBox, Profile


def task_count(id_user):
    profile = Profile.objects.filter(id_user=id_user).last()
    task_box = TaskBox.objects.filter(id_user=profile).last()

    metas_all = task_box.metas + task_box.metas_pro
    return metas_all
