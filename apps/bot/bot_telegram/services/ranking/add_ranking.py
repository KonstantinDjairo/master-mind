from apps.bot.models import Edition, Profile, DoneList, Ranking


def create_ranking(profile, points_metas, edition, metas, metas_pro):
    """
    create_ranking
    """
    try:
        points_user = points_metas.metas + points_metas.metas_pro
        instance = Ranking.objects.create(id_user=profile, points=points_user,
                                          metas=metas, metas_pro=metas_pro)
        instance.edition.add(edition)
        return True
    except ValueError as e:
        print(f"Erro create_ranking: {e}")
        return False


def update_ranking(profile, points_metas, edition, metas, metas_pro):
    """
    update_ranking
    """
    points_user = points_metas.metas + points_metas.metas_pro
    try:
        ranking = Ranking.objects.filter(pk=profile.pk, edition=edition.pk).last()
        ranking.points = ranking.points + points_user
        ranking.metas = ranking.metas + metas
        ranking.metas_pro = ranking.metas_pro + metas_pro
        ranking.save()
        return True
    except ValueError as e:
        print(f"Erro update_ranking: {e}")
        return False


def ranking_conf(id_user, metas, metas_pro):
    edition = Edition.objects.filter(active=True).last()
    profile = Profile.objects.filter(id_user=id_user).first()
    if not edition or not profile:
        return False

    points_metas = DoneList.objects.filter(id_user=profile.pk,
                                           edition=edition).last()

    ranking = Ranking.objects.filter(id_user=profile.pk,
                                     edition=edition).last()

    if ranking:
        return update_ranking(profile, points_metas, edition, metas, metas_pro)
    else:
        return create_ranking(profile, points_metas, edition, metas, metas_pro)
