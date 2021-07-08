from django.db import models


class MetasCompleted(models.Model):
    user_name = models.CharField(null=False, unique=True, max_length=255, blank=False)

    metas = models.FloatField(blank=True, default=0)
    metas_pro = models.FloatField(blank=True, default=0)

    streak = models.BooleanField(blank=True)
    streak_count = models.IntegerField(blank=True, default=0)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class MetasIncomplete(models.Model):

    user_name = models.CharField(null=False, unique=True, max_length=255, blank=False)

    metas = models.FloatField(blank=True, default=0)
    metas_pro = models.FloatField(blank=True, default=0)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
