from django.db import models


class Profile(models.Model):
    # user_name do telegram como user                         
    user_name = models.CharField(null=False, unique=True, max_length=255, blank=False)
   
    first_name = models.CharField(max_length=200, blank=True, default="...")
    last_name = models.CharField(max_length=200, blank=True, default="...")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_name
  

class MetasCompleted(models.Model):
    user_name = models.ForeignKey(Profile, on_delete=models.PROTECT)

    metas = models.FloatField(blank=True, default=0)
    metas_pro = models.FloatField(blank=True, default=0)

    streak = models.BooleanField(blank=True)
    streak_count = models.IntegerField(blank=True, default=0)
    streak_max = models.IntegerField(blank=True, default=0)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_name)


   
    
class MetasIncomplete(models.Model):
    user_name = models.ForeignKey(Profile, on_delete=models.PROTECT)

    metas = models.FloatField(blank=True, default=0)
    metas_pro = models.FloatField(blank=True, default=0)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_name)


