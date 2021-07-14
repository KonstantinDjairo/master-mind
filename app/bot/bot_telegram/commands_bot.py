from app.bot.bot_telegram.bot_filters import response_metas_complete,\
    response_metas_incomplete
from app.bot.bot_telegram.services.check_profile import check_profile_exists, check_profile_active, \
    check_time_task_box
from app.bot.bot_telegram.services.create_profile import create_profile


def create(mensage, username):
    status = create_profile(mensage, username)
    if status:
        return "Criado"
    else:
        return "ERRO ao criar o perfil!!!"


def task_box(mensage, user_name):
    exists = check_profile_exists(user_name)
    if not exists:
        return "User não existe \n/c 🤝"
    check_time = check_time_task_box()
    # if not cheak_time
    if check_time:
        return "Ja passou das 10 horas"

    active = check_profile_active(user_name)
    if not active:
        return "User Bloqueado"

    status = response_metas_incomplete(mensage, user_name)
    if status:
        return f"Tudo OK:\nParabens: {user_name} "
    else:
        return f"ERRO!!! DOTLIST"


def done_list(mensage, user_name):
    exists = check_profile_exists(user_name)
    if not exists:
        return "User não existe"
    active = check_profile_active(user_name)
    if not active:
        return "User Bloqueado"
    status = response_metas_complete(mensage, user_name)

    if status:
        return f"Tudo OK:\nParabens: {user_name} "
    else:
        return "ERRO"


