from apps.bot.models import Edition, Profile, DoneList, Ranking


def create_ranking(profile, done_list, edition, metas, metas_pro):
    """
    create_ranking
    """
    points_user = (done_list.metas / 10) + (done_list.metas_pro / 10)

    metas = metas / 10
    metas_pro = metas_pro / 10
    metas = round(metas, 2)
    metas_pro = round(metas_pro, 2)
    points_user = round(points_user, 2)
    try:
        instance = Ranking.objects.create(id_user=profile, points=points_user,
                                          metas=metas, metas_pro=metas_pro)
        instance.edition.add(edition)
        return True
    except Exception as e:
        print(f"Erro create_ranking: {e}")
        return False


def update_ranking(profile, done_list, edition, metas, metas_pro):
    """
    update_ranking
    """
    points = 0
    metas_done_list = done_list.metas / 10
    metas_pro_list = done_list.metas_pro / 10
    points_user = metas_done_list + metas_pro_list

    metas = metas / 10
    metas_pro = metas_pro / 10
    metas = round(metas, 2)
    metas_pro = round(metas_pro, 2)

    #try:
    ranking = Ranking.objects.filter(id_user=profile.pk,
                                        edition=edition.pk).last()

    ranking.points = ranking.points + points_user
    ranking.metas = ranking.metas + metas
    ranking.metas_pro = ranking.metas_pro + metas_pro
    ranking.save()

    return True
    # except Exception as e:
    #     print(f"Erro update_ranking: {e}")
    #     return False


def ranking_conf(id_user, metas, metas_pro):
    edition = Edition.objects.filter(active=True).last()
    profile = Profile.objects.filter(id_user=id_user).last()

    done_list = DoneList.objects.filter(id_user=profile.pk,
                                        edition=edition).last()

    ranking = Ranking.objects.filter(id_user=profile.pk,
                                     edition=edition).last()

    if ranking:
        return update_ranking(profile, done_list, edition, metas, metas_pro)
    else:
        return create_ranking(profile, done_list, edition, metas, metas_pro)
