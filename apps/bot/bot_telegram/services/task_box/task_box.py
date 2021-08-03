from .task_box_create import create_task_box


def add_metas_task_box(id_user, metas, metas_pro):
    """
    ADD task box
    """
    return create_task_box(id_user, metas, metas_pro)

