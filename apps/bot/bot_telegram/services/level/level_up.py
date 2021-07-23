from django.utils import timezone

from apps.bot.models import Level, DoneList, Ranking, Profile, Edition,\
    LevelUser


def level_user_To_edit(number, profile):

    try:
        level_user = LevelUser.objects.filter(id_user=profile.pk).last()
        level = Level.objects.filter(number=number).last()
        level_user.level = level
        level_user.number = level.number
        level_user.save(force_update=True)
        return True
    except ValueError as e:
        print(f"Erro level_user_To_edit: {e}")
        return False


def level_check(id_user):
    points = 0
    level_current = None
    profile = Profile.objects.filter(id_user=id_user).last()
    ranking = Ranking.objects.filter(id_user=profile.pk)
    level = Level.objects.all()

    for _ in ranking:
        points = points + _.points

    for _ in level:
        if points >= _.points <= points:
            level_current = _.number
            break
    if level_current:
        return level_current
    return False


def level_check_up(id_user):
    profile = Profile.objects.filter(id_user=id_user).last()
    level_user = LevelUser.objects.filter(id_user=profile.pk).last()

    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')

    if current_data == level_user.updated.strftime('%d/%m/%Y'):
        return f"Parabens {profile.user_name} você pro Nivel {level.number}"
    else:
        return f"Parabens {profile.user_name}"

