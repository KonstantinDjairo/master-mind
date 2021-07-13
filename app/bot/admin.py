from django.contrib import admin
from app.bot.models import MetasCompleted, MetasIncomplete, Profile, Ranking, Edition
# Register your models here.

admin.site.register(MetasCompleted)
admin.site.register(MetasIncomplete)
admin.site.register(Profile)
admin.site.register(Ranking)
admin.site.register(Edition)