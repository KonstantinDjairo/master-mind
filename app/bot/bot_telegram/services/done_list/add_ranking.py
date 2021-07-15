from app.bot.models import Edition, Profile, MetasCompleted, Ranking


def add_ranking(user_name):
    points_user = 0
    edition = Edition.objects.filter(active=True).first()
    user = Profile.objects.filter(user_name=user_name).first()
    points_metas = MetasCompleted.objects.filter(user_name=user_name)

    for points in points_metas:
        points_user += points.metas + points.metas_pro

    try:
        Ranking.objects.create(user_name=user, points=points_user,
                               edition=edition)
        return True
    except:
        return False
