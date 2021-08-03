from django.contrib import admin
from apps.bot.models import DoneList, TaskBox, Profile, Ranking,\
    Edition, Level, LevelUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'icon', 'active', 'created']
    search_fields = ['user_name']
    ordering = ['-created']


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'points',]
    ordering = ['-points']


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['title', 'points', 'metas', 'metas_pro']


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'active', 'start', 'end']
    ordering = ['-number']
    search_fields = ['title']


@admin.register(LevelUser)
class LevelUserAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'level', 'prestige_level', 'prestige']
    ordering = ['-number']


@admin.register(DoneList)
class DoneListAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'edition', 'streak', 'streak_count', 'streak_max', 'updated']
    ordering = ['-streak_max']


@admin.register(TaskBox)
class TaskBoxAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'edition', 'updated']