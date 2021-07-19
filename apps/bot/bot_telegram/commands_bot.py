from apps.bot.bot_telegram.message_filters.filter_done_list import \
    response_done_list
from apps.bot.bot_telegram.message_filters.filter_task_box import\
    response_task_box
from apps.bot.bot_telegram.services.profile.check_profile import \
    check_profile_exists, check_profile_active, check_time_task_box
from apps.bot.bot_telegram.services.profile.create_profile import create_profile
from apps.bot.bot_telegram.services.done_list.check_done_list import\
    check_done_list_exists
from apps.bot.bot_telegram.services.task_box.check_task_bot import \
    check_task_exists
from apps.bot.bot_telegram.services.edition.check_edition_active import \
    edition_active


def create(message, user_name, id_user):
    """
    create profile with the id_user from the telegram and an
    emoji chosen by the user,
    if the user does not choose an emoji and set a default
    """
    if check_profile_exists(id_user):
        return f"Você ja tem um perfil '{user_name}', ja pode mandar sua" \
               f" Task Box"

    if create_profile(message, user_name, id_user):
        return "Criado, agora pode mandar sua task box"

    else:
        return "ERRO!!! Ao criar o perfil, fale com o ADM!!!"


def task_box(message, user_name, id_user):
    """
    create a task box, with the message and the user
    """

    if not check_profile_exists(id_user):
        return "User não existe \n/c 🤝"

    elif not check_time_task_box():
        return "Ja passou das 10 horas"

    elif not check_profile_active(id_user):
        return "User Bloqueado"

    elif not edition_active():
        return "Não a nenhuma edição ativa"

    elif check_task_exists(id_user):
        return "Você ja adicionou task box hoje"

    elif response_task_box(message, id_user):
        return f"Tudo OK:\nParabens: {user_name}"

    else:
        return f"ERRO!!! Task box, fale com o ADM!!!"


def done_list(message, user_name, id_user):
    """
    create a done list , with the message and the user
    """
    if not check_profile_exists(id_user):
        return "User não existe"

    elif not check_profile_active(id_user):
        return "User Bloqueado"

    elif not edition_active():
        return "Não a nenhuma edição ativa"

    elif not check_task_exists(user_name):
        return "Você não adicionou a task box de hoje "

    elif check_done_list_exists(id_user):
        return "Você ja adicionou done_list hoje "

    elif response_done_list(message, id_user):
        return f"Tudo OK:\nParabens: {user_name}"
    else:
        return "ERRO!!! Done List, fale com o ADM!!!"


