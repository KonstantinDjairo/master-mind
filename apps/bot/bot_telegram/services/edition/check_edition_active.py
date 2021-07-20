from apps.bot.models import Edition


def edition_active():
    """
    edition_active
    """
    edition = Edition.objects.filter(active=True)

    if edition:
        return True
    else:
        return False
