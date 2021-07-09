from django.utils import timezone
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
    streak_count = 0
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
    # aaa
    return False


def add_metas_completed(user_name, streak, metas, metas_x, metas_pro, metas_pro_x):
    metas_exists = MetasIncomplete.objects.filter(user_name=user_name)

    if metas_exists:
        add_metas(metas_exists, user_name,  streak, metas, metas_x, metas_pro, metas_pro_x)
        return True
    # se metas não existir ele vai quebrar o passo.
    else:
        return False


def add_metas_incomplete(user_name, metas, metas_pro):
    current_data = timezone.now()
    user_exists = MetasIncomplete.objects.filter(user_name=user_name)
    # datetime.date.today()
    if not user_exists:
        MetasIncomplete.objects.create(user_name=user_name, metas=metas, metas_pro=metas_pro)
        return True
    else:
        for dado in user_exists:
            pk = dado.pk
            data_time = dado.updated
               
        print(current_data.strftime('%d/%m/%Y') + " -- " + data_time.strftime('%d/%m/%Y'))
        if not current_data.strftime('%d/%m/%Y') == data_time.strftime('%d/%m/%Y'):
            metas_incomplete = MetasIncomplete.objects.get(pk=pk)
            metas_incomplete.metas =  metas
            metas_incomplete.metas_pro = metas_pro
            metas_incomplete.save(force_update=True)
            return True
        else:
            return False
