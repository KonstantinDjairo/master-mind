from apps.bot.models import Profile, LevelUser, Level


def prestige_check(profile):
    level_user = LevelUser.objects.filter(id_user=profile).last()
    
    if level_user.prestige:
        return True
    return False


def level_user_to_edit_prestige(profile):
    try:
        level_user = LevelUser.objects.filter(id_user=profile.pk).last()
        level = Level.objects.filter().first()
        print(level)
        level_user.level = level
        level_user.number = level.number
        level_user.prestige_level += 1
        level_user.save(force_update=True)
        
        return True
    except Exception as e:
        print(f"Erro level_user_to_edit_prestige: {e}")
        return False


def prestige(profile):
    pass