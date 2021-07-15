from app.bot.bot_telegram.bot_filters import response_metas_complete,\
    response_metas_incomplete
from app.bot.bot_telegram.services.check_profile import check_profile_exists,\
    check_profile_active, check_time_task_box
from app.bot.bot_telegram.services.create_profile import create_profile
from app.bot.bot_telegram.services.task_box.check_task_bot import check_task_exists


def create(message, username):
    status = create_profile(message, username)
    if status:
        return "Criado, agora pode mandar sua task box"
    else:
        return "ERRO ao criar o perfil!!!"


def task_box(message, user_name):
    if not check_profile_exists(user_name):
        return "User não existe \n/c 🤝"

    elif not check_time_task_box():
        return "Ja passou das 10 horas"

    elif not check_profile_active(user_name):
        return "User Bloqueado"

    elif response_metas_incomplete(message, user_name):
        return f"Tudo OK:\nParabens: {user_name} "
    else:
        return f"ERRO!!! task box"


def done_list(message, user_name):
    if not check_profile_exists(user_name):
        return "User não existe"

    elif not check_profile_active(user_name):
        return "User Bloqueado"
    elif not check_task_exists(user_name):
        return "Você não adicionou a task box de hoje "

    elif response_metas_complete(message, user_name):
        return f"Tudo OK:\nParabens: {user_name}"
    else:
        return "ERRO!!! done list"


