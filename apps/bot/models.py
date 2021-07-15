from django.db import models


class Profile(models.Model):
    # user_name do telegram como user                         
    user_name = models.CharField(null=False, unique=True, max_length=100, blank=False)
   
    first_name = models.CharField(max_length=100, blank=True, default="...")
    last_name = models.CharField(max_length=100, blank=True, default="...")
    icon = models.CharField(max_length=1, blank=True, default="🙂")
    
    active = models.BooleanField(null=False, default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_name


class Edition(models.Model):

    title = models.CharField(max_length=100, null=False, default='Edition')
    description = models.TextField(default="Description....")

    number = models.IntegerField(null=False, blank=False, unique=True)
    active = models.BooleanField(null=False, default=True)

    class Meta:
        ordering = ["-number"]

    def __str__(self):
        return str(self.title)


class Ranking(models.Model):
    user_name = models.ForeignKey(Profile, on_delete=models.PROTECT)
    points = models.IntegerField(null=False, blank=False, default=0)
    edition = models.ManyToManyField(Edition)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-points"]

    def __str__(self):
        return str(self.user_name)

    
class MetasCompleted(models.Model):
    user_name = models.ForeignKey(Profile, on_delete=models.PROTECT)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
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
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
      
    metas = models.FloatField(blank=True, default=0)
    metas_pro = models.FloatField(blank=True, default=0)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_name)
    


