from django.utils import timezone

from apps.bot.models import Level, DoneList, Ranking, Profile, Edition,\
    LevelUser


def level_user_to_edit(number, profile):
    print(number)
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


def level_check(profile):
    """
    check up nivel
    """
    points = 0
    level_current = None

    ranking = Ranking.objects.filter(id_user=profile.id_user)

    level = Level.objects.order_by("number")

    print(ranking)
    for _ in ranking:
        points = points + _.points

    for _ in level:
        print(_.number)
        if points >= _.points <= points:
            level_current = _.number

    if level_current:
        return level_current
    return False


def level_check_up(id_user):
    """
    level_check_up
    """
    profile = Profile.objects.filter(id_user=id_user).last()
    level_user = LevelUser.objects.filter(id_user=profile.pk).last()
    print(level_user.number)
    level = Level.objects.filter(number=level_user.number).first()
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')
    print(level)
    if current_data == level_user.updated.strftime('%d/%m/%Y'):
        return f""" 🔥 Parabéns ao Guerreiro que subiU de nível! 
😁:User
___
{level.title}:
+1 Meta
+1 ProMode

⚔️:{profile.user_name}
_

👉🏻 Vocês poderão adicionar as suas novas atribuições a partir do próximo envio da TaskBox.
_
"""
    else:
        return f"Parabens {profile.user_name}"


