import re

from apps.bot.bot_telegram.services.done_list.done_list import\
    add_metas_done_list
from apps.bot.bot_telegram.services.task_box.task_count import task_count


def filter_done_list(message, id_user):
    """
        ✅ ou ❌
        é isso ai
        :param message:
        :param id_user:
        :return: boolean
    """
    streak = True
    global metas_pro, metas_pro_x, start
    if "ProMode" in message:
        pro_mode = re.search(r"ProMode", message)
        start = pro_mode.start()
        end = len(message)
        message_pro_mode = message[start:end]

        meta_pro_list_completed = re.findall('✅', message_pro_mode)
        metas_pro_list_x = re.findall('❌', message_pro_mode)

        metas_pro = len(meta_pro_list_completed)
        metas_pro_x = len(metas_pro_list_x)

    if "❌" in message:
        streak = False

    if "Metas" in message:
        metas_list = re.findall("✅", message[0:start])
        metas = len(metas_list)
    else:
        return False

    return add_metas_done_list(id_user, streak, metas, metas_pro)


def check_done(message, id_user):

    metas_max = re.findall("✅", message)
    metas_max_done = len(metas_max)
    metas_max_task = task_count(id_user)

    if not metas_max_done <= metas_max_task:
        return True
    else:
        return False


