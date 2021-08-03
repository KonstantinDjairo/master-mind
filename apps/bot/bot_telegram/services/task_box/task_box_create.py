from apps.bot.models import TaskBox, Profile, Edition


def create_task_box(id_user, metas, metas_pro):
    try:
        edition = Edition.objects.filter(active=True).last()
        profile = Profile.objects.filter(id_user=id_user).last()
        TaskBox.objects.create(id_user=profile, metas=metas,
                               metas_pro=metas_pro, edition=edition)
        return True
    except Exception as e:
        print(f"Erro create_task_box: {e}")
        return False
