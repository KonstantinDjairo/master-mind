import re
from apps.bot.bot_telegram.services.task_box.task_box import \
    add_metas_task_box


def filter_task_box(message):
    """
        ⏱
        é isso ai
        :param message:
        :return: lista
    """
    global metas_pro, start, metas
    lista = []

    if "ProMode" in message:
        pro_mode = re.search(r"ProMode", message)
        start = pro_mode.start()
        end = len(message)
        message_pro_mode = message[start:end]
        meta_pro_list_incomplete = re.findall("⏱", message_pro_mode)
        metas_pro = len(meta_pro_list_incomplete)

    if "Metas" in message:
        metas_list = re.findall("⏱", message[0:start])
        metas = len(metas_list)
    lista.append({"metas": metas, "metas_pro": metas_pro})

    return lista


def task_box_list(message, id_user):
    if not "Metas" in message or not "⏱" in message:
        return "A mensagem é invalida, por favor segue a padrao da task box"

    lista = filter_task_box(message)

    meta = lista[0]["metas"]
    metas_p = lista[0]["metas_pro"]

    if add_metas_task_box(id_user, meta, metas_p):
        return "Tudo ok, Boa sorte"
    else:
        return f"ERRO!!! Task box, fale com o ADM!!!"
