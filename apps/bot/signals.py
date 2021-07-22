from django.db.models.signals import post_save, pre_delete

from apps.bot.models import Level, LevelUser, Profile


def create_level_user(sender, instance, created, **kwargs):
    level = Level.objects.filter().first()
    if created:
        LevelUser.objects.create(id_user=instance, level=level, check=False)
    else:
        if not hasattr(instance, "profile"):
            LevelUser.objects.create(id_user=instance, level=level, check=False)


post_save.connect(create_level_user, sender=Profile)

