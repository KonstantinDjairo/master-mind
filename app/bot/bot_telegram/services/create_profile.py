from app.bot.bot_telegram.services.check_profile import check_profile_exists
from app.bot.models import Profile


def create_profile(mensage, user_name):
    icon = mensage[3]
    size = len(icon)
    if check_profile_exists(user_name):
        return False
    elif size == 1:
        Profile.objects.create(user_name=user_name, icon=icon)
        return True
    elif not check_profile_exists(user_name):
        Profile.objects.create(user_name=user_name)
        return True
    else:
        return False