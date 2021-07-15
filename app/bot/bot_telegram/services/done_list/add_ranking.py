from app.bot.models import Edition, Profile, MetasCompleted, Ranking


def create_ranking(profile, points_user, edition):
    Ranking.objects.create(user_name=profile, points=points_user,
                           edition=edition)
    return True


def update_ranking(profile, points_user, edition):
    ranking = Ranking.objects.get(pk=profile.pk, edition=edition.pk)

    ranking.points = ranking.points + points_user
    ranking.save()
    return True


def ranking_conf(user_name):
    points_user = 0
    edition = Edition.objects.filter(active=True).first()
    profile = Profile.objects.filter(user_name=user_name).first()
    if not edition or not profile:
        return False

    points_metas = MetasCompleted.objects.get(user_name=user_name)
    for points in points_metas:
        points_user += points.metas + points.metas_pro

    ranking = Ranking.objects.filter(user_name=profile, edition=edition) \
        .first()

    if ranking:
        return update_ranking(profile, points_user, edition)
    else:
        return create_ranking(profile, points_user, edition)
