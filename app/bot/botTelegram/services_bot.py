from ..models import MetasCompleted, MetasIncomplete

def check_metas(metas_exists, metas, metas_pro, ):
    for dado in metas_exists:
        metas_ = dado.metas
        metas_pro_ = dado.metas_pro
        updated_ = dado.updated

    if metas_ == metas and metas_pro_ == metas_pro:
        return True
    else:
        return False


def add_metas(metas_exists, user_name, streak, metas, metas_x, metas_pro, metas_pro_x):
    metas_completed = MetasCompleted.objects.filter(user_name=user_name)
    metas_ok = check_metas(metas_exists, metas, metas_pro)
    if not metas_completed:
        if metas_ok:
            MetasCompleted.objects.create(user_name=user_name, metas=metas, metas_pro=metas_pro, streak=streak,
                                          streak_count=streak_count + 1)
            return True
        else:
            MetasCompleted.objects.create(user_name=user_name, metas=metas, metas_pro=metas_pro, streak=streak,
                                              streak_count=0)
            return True
    else:
        for dado in metas_completed:
            pk = dado.pk
            metas_user = dado.metas
            metas_pro_user = dado.metas_pro
            streak_count_user = dado.streak_count

        metas_completed = MetasCompleted.objects.get(pk=pk)
        # repetinção de codigo, eu sei
        if metas_ok:
            metas_completed.metas = metas_user + metas
            metas_completed.metas_pro = metas_pro + metas_pro_user
            metas_completed.streak_count += 1
            metas_completed.streak = streak
            metas_completed.save()
        else:
            metas_completed.metas = metas_user + metas
            metas_completed.metas_pro = metas_pro + metas_pro_user
            metas_completed.streak_count = 0
            metas_completed.streak = False
            metas_completed.save()
        return True




def add_metas_completed(user_name, streak, metas, metas_x, metas_pro, metas_pro_x):
    metas_exists = MetasIncomplete.objects.filter(user_name=user_name)

    if metas_exists:
        status = add_metas(metas_exists, user_name,  streak, metas, metas_x, metas_pro, metas_pro_x)
        return True
    else:

        return False


def add_metas_incomplete(user_name, metas, metas_pro):
    user_exists = MetasIncomplete.objects.filter(user_name=user_name)

    if not user_exists:
        MetasIncomplete.objects.create(user_name=user_name, metas=metas, metas_pro=metas_pro)
    else:
        for dado in user_exists:
            pk = dado.pk

        metas_incomplete = MetasIncomplete.objects.get(pk=pk)
        metas_incomplete.metas =  metas
        metas_incomplete.metas_pro = metas_pro
        metas_incomplete.save(force_update=True)




















