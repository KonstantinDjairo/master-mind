import re

from app.bot.botTelegram.services_bot import (add_metas_completed,
                                              add_metas_incomplete, create_profile_user, check_profile_exists)


def filter_modes_complete(mensage, user_name):
    """
        ✅ ou ❌
        é isso ai
        :param mensage:
        :param username:
        :return: lista
    """
    streak = True
    global metas_pro, metas_pro_x, start
    if "ProMode" in mensage:
        pro_mode = re.search(r"ProMode", mensage)
        start = pro_mode.start()
        end = len(mensage)
        mensage_pro_mode = mensage[start:end]

        meta_pro_list_completed = re.findall("✅", mensage_pro_mode)
        metas_pro_list_x = re.findall("❌", mensage_pro_mode)

        metas_pro = len(meta_pro_list_completed)
        metas_pro_x = len(metas_pro_list_x)

    if "❌" in mensage:
        streak = False

    if "Metas" in mensage:
        metas_list = re.findall("✅", mensage[0:start])
        metas_list_x = re.findall("❌", mensage[0: start])

        metas = len(metas_list)
        metas_x = len(metas_list_x)
    else:
        return False

    status = add_metas_completed(user_name, streak, metas, metas_x, metas_pro, metas_pro_x)
    if status:
        return True
    else:
        return False


def response_metas_complete(mensage, username):
    metas_list_completed = re.findall("✅", mensage)
    metas_list_x = re.findall("❌", mensage)
    
    completed_metas = len(metas_list_completed)
    x_metas = len(metas_list_x)

    status_ok = filter_modes_complete(mensage, username)

    if status_ok:
        return f"Tudo OK:\nParabens: {username} você concluiu: {completed_metas} \n E não concluiu: {x_metas} "
    else:
        return f"""ERRO!!\nOla{username}!!\nos possoveis erros são:> Não mandou a lista de metas a comprir\n
        > A lista de metas esta errada, verifique a mensagem e se ela esta de acordo com o moude, caso esteja procure o ADM
            
        """

def filter_modes_incomplete(mensage, username):
    """
        ⏱
        é isso ai
        :param mensage:
        :param username:
        :return: lista
    """

    global metas_pro, start
    if "ProMode" in mensage:
        pro_mode = re.search(r"ProMode", mensage)
        start = pro_mode.start()
        end = len(mensage)
        mensage_pro_mode = mensage[start:end]
        meta_pro_list_incomplete = re.findall("⏱", mensage_pro_mode)
        metas_pro = len(meta_pro_list_incomplete)

    if "Metas" in mensage:
        metas_list = re.findall("⏱", mensage[0:start])
        metas = len(metas_list)
    else:
        return False

    status =  add_metas_incomplete(username, metas, metas_pro)
    if status:
        return True
    else:
        return False


def response_metas_incomplete(mensage, username):
    """
        funtion
    """
    metas_list_incomplete = re.findall("⏱", mensage)
    incomplete_metas = len(metas_list_incomplete)

    status_ok = filter_modes_incomplete(mensage, username)

    if status_ok:
        return f"Tudo OK:\n{username} você tem {incomplete_metas} para concluir, boa sorte!!!"
    else:
        return f"""ERRO!!\n
            Ola{username}!!
            os possoveis erros são:\n
            Mensagem fora do padrão
        """


def create_profile(username):
    status_ok = create_profile_user(username)
    if status_ok:
        return "Pefil criado com sucesso"
    else:
        return "ERRO!!!\nPerfil já existe"
    

def chek_profile(user_name):
    profile = check_profile_exists(user_name)
    if profile:
        return True
    else:
        return False

        