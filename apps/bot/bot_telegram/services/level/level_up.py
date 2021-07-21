from apps.bot.models import Level, DoneList, Ranking, Profile, Edition,\
    LevelUser


def level_user_To_edit(number, profile):

    try:
        level_user = LevelUser.objects.filter(id_user=profile.pk).last()
        level = Level.objects.filter(number=number).last()
        level_user.level = level
        level.save()
        return True
    except ValueError as e:
        print(f"Erro level_user_To_edit: {e}")
        return False


def level_check_up(id_user):
    number = 0
    points = 0
    profile = Profile.objects.filter(id_user=id_user).last()
    ranking = Ranking.objects.filter(id_user=profile.pk)
    level = Level.objects.all()

    for _ in ranking:
        points += _.points

    for _ in level:
        if points < _.points >= points:
            number = _.number
            break

    level = Level.objects.filter(number=number-2).last()
    if points >= level.points:
        level_user_To_edit(number, profile)
        return f"Parabens {profile.user_name} você pro Nivel {level.number}"
    else:
        return f"Parabens {profile.user_name}"

