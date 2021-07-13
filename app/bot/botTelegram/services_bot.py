from django.utils import timezone

from ..models import MetasCompleted, MetasIncomplete, Profile


def check_profile_exists(user_name):

    profile_exists = Profile.objects.filter(user_name=user_name)
    if profile_exists:
        return True
    else:
        return False


def create_profile_user(user_name):
    user_exists = Profile.objects.filter(user_name=user_name)
    if not user_exists:
        Profile.objects.create(user_name=user_name)
        return True
    else:
        return False


def check_time_task_box():
    time_str = timezone.now()
    time = int(time_str.strftime('%H'))
    print(time)
    if time < 10:
        print("abaixo das 10 horas")
        return True
    else:
        return False
    

def check_metas(metas_exists, metas, metas_pro ):
    for dado in metas_exists:
        metas_ = dado.metas
        metas_pro_ = dado.metas_pro
        updated_ = dado.updated

    if metas_ == metas and metas_pro_ == metas_pro:
        return True
    else:
        return False


def add_metas(metas_exists, user_name, streak, metas, metas_x, metas_pro, metas_pro_x):
    current_data = timezone.now()
    streak_count = 0  
     
    user = Profile.objects.filter(user_name=user_name).first()
    metas_user = MetasCompleted.objects.filter(user_name=user.pk).first()
    metas_ok = check_metas(metas_exists, metas, metas_pro)

    if not metas_user:
        if metas_ok:
            MetasCompleted.objects.create(user_name=user, metas=metas,
                                          metas_pro=metas_pro, streak=streak,
                                          streak_count=streak_count + 1,
                                          streak_max = 1)
            return True
        else:
            MetasCompleted.objects.create(user_name=user, metas=metas, 
                                          metas_pro=metas_pro, streak=streak,
                                            streak_count=0, streak_max = 0)
            return True
    else:
        if not current_data.strftime('%d/%m/%Y') == metas_user.updated.strftime('%d/%m/%Y'):
            metas_completed = MetasCompleted.objects.get(pk=metas_user.pk)
            # repetição de codigo, eu sei
            if metas_ok:
                metas_completed.metas = metas_user.metas + metas
                metas_completed.metas_pro = metas_user.metas_pro + metas_pro
                metas_completed.streak_count += 1
                metas_completed.streak = streak
                metas_completed.streak_max += 1
                metas_completed.save()
            else:
                metas_completed.metas = metas_user.metas + metas
                metas_completed.metas_pro = metas_user.metas_pro + metas_pro
                metas_completed.streak_count = 0
                metas_completed.streak = False
                metas_completed.save()
            return True
        else:
            return False


def add_metas_completed(user_name, streak, metas, metas_x, metas_pro, metas_pro_x):
    user = Profile.objects.filter(user_name=user_name).first()
    metas_exists = MetasIncomplete.objects.filter(user_name=user.pk)
  
    if metas_exists:
        status_ok = add_metas(metas_exists, user_name,  streak, metas,
                              metas_x, metas_pro, metas_pro_x)
        if status_ok:
            return True
        else:
            return False
    else:
        return False


def add_metas_incomplete(user_name, metas, metas_pro):
    current_data = timezone.now()
    
    user = Profile.objects.filter(user_name=user_name).first()
    user_metas = MetasIncomplete.objects.filter(user_name=user.pk).first()
    status_ok = check_time_task_box()
    
    if not status_ok:
        return False
    elif not user_metas:
        MetasIncomplete.objects.create(user_name=user, metas=metas,
                                       metas_pro=metas_pro)
        return True
    else:
        if not current_data.strftime('%d/%m/%Y') == user_metas.updated.strftime('%d/%m/%Y'):
            metas_incomplete = MetasIncomplete.objects.get(pk=user_metas.pk)
            metas_incomplete.metas =  metas
            metas_incomplete.metas_pro = metas_pro
            metas_incomplete.save(force_update=True)
            return True
        else:
            return False
    

