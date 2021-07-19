from django.contrib import admin
from apps.bot.models import DoneList, TaskBox, Profile, Ranking, Edition

# Register your models here.

admin.site.register(DoneList)
admin.site.register(TaskBox)
admin.site.register(Profile)
admin.site.register(Ranking)
admin.site.register(Edition)
