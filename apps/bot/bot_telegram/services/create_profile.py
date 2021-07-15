import re

from apps.bot.bot_telegram.services.check_profile import check_profile_exists
from apps.bot.models import Profile


def filter_emoji(message):
    """
    regex to filter the emoji
    """
    icon = re.sub('\/c ', "", message)

    if 1 == len(icon):
        return icon
    else:
        return "🌏"


def create_profile(message, user_name):
    """
    function for creating the profile with the user name of the telegram
    """
    try:
        icon = filter_emoji(message)
        Profile.objects.create(user_name=user_name, icon=icon)
        return True
    except:
        return False


