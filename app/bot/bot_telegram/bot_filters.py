import re

from app.bot.bot_telegram.services.done_list.done_list import \
    add_metas_completed
from app.bot.bot_telegram.services.task_box.task_box import \
    add_metas_task_box


def filter_modes_complete(message, user_name):
    """
        ✅ ou ❌
        é isso ai
        :param message:
        :param user_name:
        :return: lista
    """
    streak = True
    global metas_pro, metas_pro_x, start
    if "ProMode" in message:
        pro_mode = re.search(r"ProMode", message)
        start = pro_mode.start()
        end = len(message)
        mensage_pro_mode = message[start:end]

        meta_pro_list_completed = re.findall("✅", mensage_pro_mode)
        metas_pro_list_x = re.findall("❌", mensage_pro_mode)

        metas_pro = len(meta_pro_list_completed)
        metas_pro_x = len(metas_pro_list_x)

    if "❌" in message:
        streak = False

    if "Metas" in message:
        metas_list = re.findall("✅", message[0:start])
        metas = len(metas_list)
    else:
        return False

    if add_metas_completed(user_name, streak, metas, metas_pro):
        return True
    else:
        return False


def filter_modes_incomplete(message, user_name):
    """
        ⏱
        é isso ai
        :param mensage:
        :param user_name:
        :return: lista
    """
    global metas_pro, start
    if "ProMode" in message:
        pro_mode = re.search(r"ProMode", message)
        start = pro_mode.start()
        end = len(message)
        mensage_pro_mode = message[start:end]
        meta_pro_list_incomplete = re.findall("⏱", mensage_pro_mode)
        metas_pro = len(meta_pro_list_incomplete)

    if "Metas" in message:
        metas_list = re.findall("⏱", message[0:start])
        metas = len(metas_list)
    else:
        return False

    return add_metas_task_box(user_name, metas, metas_pro)


def response_metas_incomplete(message, user_name):
    """
    response_metas_incomplete
    """
    return filter_modes_incomplete(message, user_name)


def response_metas_complete(message, user_name):
    """
    response_metas_complete
    """
    return filter_modes_complete(message, user_name)



