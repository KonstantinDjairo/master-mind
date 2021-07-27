from apps.bot.models import Edition


def edition_active():
    """
    edition_active
    """
    edition = Edition.objects.filter(active=True).last()

    if edition:
        return True
    else:
        return False
