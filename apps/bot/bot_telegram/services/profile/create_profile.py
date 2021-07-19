import re

from apps.bot.models import Profile


def filter_emoji(message):
    """
    regex to filter the emoji
    """
    try:
        icon = re.sub('\/c ', "", message)

        if 1 == len(icon):
            return icon

    except ValueError as e:
        print(f"ERRO, filter_emoji: {e}")
        return "🌏"


def create_profile(message, user_name, id_user):
    """
    function for creating the profile with the user name of the telegram
    """
    try:
        icon = filter_emoji(message)
        Profile.objects.create(id_user=id_user, user_name=user_name, icon=icon)
        return True
    except ValueError as e:
        print(f"ERRO, create_profile: {e}")
        return False


