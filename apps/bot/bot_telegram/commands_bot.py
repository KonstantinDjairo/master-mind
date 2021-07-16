from apps.bot.bot_telegram.message_filters.filter_done_list import \
    response_done_list
from apps.bot.bot_telegram.message_filters.filter_task_box import\
    response_task_box
from apps.bot.bot_telegram.services.check_profile import \
    check_profile_exists, check_profile_active, check_time_task_box
from apps.bot.bot_telegram.services.create_profile import create_profile
from apps.bot.bot_telegram.services.done_list.check_done_list import\
    check_done_list_exists
from apps.bot.bot_telegram.services.task_box.check_task_bot import \
    check_task_exists


def create(message, user_name):
    """
    create profile with the user_name from the telegram and an
    emoji chosen by the user,
    if the user does not choose an emoji and set a default
    """
    if check_profile_exists(user_name):
        return f"Você ja tem um perfil '{user_name}', ja pode mandar sua" \
               f" Task Box"

    if create_profile(message, user_name):
        return "Criado, agora pode mandar sua task box"
    else:
        return "ERRO!!! Ao criar o perfil, fale com o ADM!!!"


def task_box(message, user_name):
    """
    create a task box, with the message and the user
    """

    if not check_profile_exists(user_name):
        return "User não existe \n/c 🤝"

    elif not check_time_task_box():
        return "Ja passou das 10 horas"

    elif not check_profile_active(user_name):
        return "User Bloqueado"

    elif check_task_exists(user_name):
        return "Você ja adicionou task box hoje"

    elif response_task_box(message, user_name):
        return f"Tudo OK:\nParabens: {user_name}"

    else:
        return f"ERRO!!! Task box, fale com o ADM!!!"


def done_list(message, user_name):
    """
    create a done list , with the message and the user
    """
    if not check_profile_exists(user_name):
        return "User não existe"

    elif not check_profile_active(user_name):
        return "User Bloqueado"

    elif not check_task_exists(user_name):
        return "Você não adicionou a task box de hoje "

    elif check_done_list_exists(user_name):
        return "Você ja adicionou done_list hoje "

    elif response_done_list(message, user_name):
        return f"Tudo OK:\nParabens: {user_name}"
    else:
        return "ERRO!!! Done List, fale com o ADM!!!"


