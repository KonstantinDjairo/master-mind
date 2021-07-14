import re

from app.bot.botTelegram.services.done_list import add_metas_completed
from app.bot.botTelegram.services.task_box import add_metas_incomplete


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
    status = add_metas_incomplete(username, metas, metas_pro)
    if status:
        return True
    else:
        return False


def response_metas_incomplete(mensage, username):
    """
    response_metas_incomplete
    """
    status = filter_modes_incomplete(mensage, username)
    return status


def response_metas_complete(mensage, username):
    """
    response_metas_complete
    """
    status = filter_modes_complete(mensage, username)
    return status



