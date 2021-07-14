from app.bot.bot_telegram.services.check_profile import check_profile_exists
from app.bot.models import Profile


def create_profile(mensage, user_name):
    user_exists = check_profile_exists(user_name)
    icon = mensage[3]
    size = len(icon)
    if user_exists:
        return False
    elif size == 1:
        Profile.objects.create(user_name=user_name, icon=icon)
        return True
    elif not user_exists:
        # inserir o icon default
        Profile.objects.create(user_name=user_name)
        return True
    else:
        return False