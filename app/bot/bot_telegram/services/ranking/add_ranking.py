from app.bot.models import Edition, Profile, MetasCompleted, Ranking


def create_ranking(profile, points_metas, edition):
    points_user = points_metas.metas + points_metas.metas_pro
    instance = Ranking.objects.create(user_name=profile, points=points_user)

    instance.edition.add(edition)
    return True


def update_ranking(profile, points_metas, edition):
    points_user = points_metas.metas + points_metas.metas_pro

    ranking = Ranking.objects.filter(pk=profile.pk, edition=edition.pk).last()

    ranking.points = ranking.points + points_user
    ranking.save()
    return True


def ranking_conf(user_name):
    edition = Edition.objects.filter(active=True).last()
    profile = Profile.objects.filter(user_name=user_name).first()
    if not edition or not profile:
        return False

    points_metas = MetasCompleted.objects.filter(user_name=profile.pk,
                                                 edition=edition).last()

    ranking = Ranking.objects.filter(user_name=profile.pk,
                                     edition=edition).last()

    if ranking:
        return update_ranking(profile, points_metas, edition)
    else:
        return create_ranking(profile, points_metas, edition)
