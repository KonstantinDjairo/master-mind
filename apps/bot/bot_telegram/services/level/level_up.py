from apps.bot.bot_telegram.services.level.level_prestige import (
    level_user_to_edit_prestige, prestige_check)
from apps.bot.models import Level, LevelUser, Profile, Ranking
from django.utils import timezone


def get_level_to_id_user(id_user):
    profile = Profile.objects.filter(id_user=id_user).last()
    level_user = LevelUser.objects.filter(id_user=profile).last()
    return level_user.number


def get_level_to_profile(profile):
    level_user = LevelUser.objects.filter(id_user=profile).last()
    return level_user.number


def level_user_to_edit(number, profile):
    try:
        level_user = LevelUser.objects.filter(id_user=profile.pk).last()
        level = Level.objects.filter(number=number).first()
        level_user.level = level
        level_user.number = level.number
        level_user.save(force_update=True)
        return True
    except Exception as e:
        print(f"Erro level_user_To_edit: {e}")
        return False


def level_check(profile):
    """
    check up nivel
    """
    points = 0
    level_current = None
    ranking = Ranking.objects.filter(id_user=profile)
    level = Level.objects.all().order_by("number")

    for _ in ranking:
        points = points + _.points

    for _ in level:
        if points >= _.points:
            level_current = _.number

    return level_current


def level_check_up(id_user):
    """
    level_check_up
    """
    current_data = timezone.now()
    current_data = current_data.strftime('%d/%m/%Y')
    points = 0
    profile = Profile.objects.filter(id_user=id_user).last()
    level_user = LevelUser.objects.filter(id_user=profile.pk).last()
    level = Level.objects.filter(number=level_user.number).first()
    ranking = Ranking.objects.filter(id_user=profile)

    for _ in ranking:
        points = points + _.points
    message = f""" 🔥 Parabéns ao Guerreiro que subiU de nível! 
😁:User
___
{level.title}:
+1 Meta
+1 ProMode
Pontos totais: {points}
⚔️:{profile.user_name}
_

👉🏻 Vocês poderão adicionar as suas novas atribuições a partir do próximo envio da TaskBox.
_
"""
    # fazer refatoração neste codigo
    if current_data == level_user.updated.strftime('%d/%m/%Y'):
        if level.number == 10:
            if not prestige_check(profile):
                return "Faça o update pra prestigio com o comando /up"
            else:
                if level_user_to_edit_prestige(profile):
                    return "Tudo ok"
                else:
                    return "Erro inesperado "
        else:
            return message
    else:
        return f"Parabens {profile.user_name}"


