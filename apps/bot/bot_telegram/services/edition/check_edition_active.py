from apps.bot.models import Edition


def edition_active():
    """
    edition_active
    """
    edition = Edition.objets.get(active=True)

    if edition:
        return True
    else:
        return False
