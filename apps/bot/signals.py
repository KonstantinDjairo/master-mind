from django.db.models.signals import post_save, pre_delete

from apps.bot.models import Level, LevelUser, Profile, Ranking
from apps.bot.bot_telegram.services.level.level_up import level_check, level_user_To_edit


def create_level_user(sender, instance, created, **kwargs):
    level = Level.objects.filter().first()
    if created:
        LevelUser.objects.create(id_user=instance, level=level, check=False)
    else:
        if not hasattr(instance, "profile"):
            LevelUser.objects.create(id_user=instance, level=level,
                                     check=False, number=0)


def update_level(sender, instance, created, **kwargs):

    if not hasattr(instance, "Ranking"):
        profile = Profile.objects.filter(user_name=instance.id_user).last()
        if not level_check(profile.id_user):
            pass
        else:
            number = level_check(profile.id_user)
            level_user_To_edit(number, profile)


post_save.connect(create_level_user, sender=Profile)
post_save.connect(update_level, sender=Ranking)
