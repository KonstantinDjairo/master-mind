from django.contrib import admin
from app.bot.models import MetasCompleted, MetasIncomplete
# Register your models here.

admin.site.register(MetasCompleted)
admin.site.register(MetasIncomplete)