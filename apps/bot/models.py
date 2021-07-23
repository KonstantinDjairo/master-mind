from django.db import models


class Profile(models.Model):
    user_name = models.CharField(null=False, unique=False, max_length=100, blank=True)
    id_user = models.IntegerField(null=False, unique=True)
    first_name = models.CharField(max_length=100, blank=True, default="...")
    last_name = models.CharField(max_length=100, blank=True, default="...")
    icon = models.CharField(max_length=10, blank=True, default="🙂")
    
    active = models.BooleanField(null=False, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name


class Level(models.Model):
    title = models.CharField(max_length=100, null=False, default='Nvl 0. Legionário')
    description = models.TextField(default="Description....")
    number = models.IntegerField(null=False, blank=False, unique=True, auto_created=True)
    points = models.IntegerField(null=False, blank=False, default=0)
    metas = models.IntegerField(blank=True, default=1)
    metas_pro = models.IntegerField(blank=True, default=1)
    prestige = models.BooleanField(null=False, default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-number"]


class Edition(models.Model):
    title = models.CharField(max_length=100, null=False, default='Edition 1')
    description = models.TextField(default="Description....")

    number = models.IntegerField(null=False, blank=False, unique=True, auto_created=True)
    active = models.BooleanField(null=False, default=True)

    start = models.DateTimeField()
    end = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-number"]

    def __str__(self):
        return f"{str(self.title)} - {self.number}"


class LevelUser(models.Model):
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    number = models.IntegerField(null=False, blank=False, default=0)
    prestige = models.BooleanField(null=False, default=False)
    prestige_level = models.IntegerField(null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_user} - {self.level}"


class Ranking(models.Model):
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    edition = models.ManyToManyField(Edition)

    points = models.FloatField(null=False, blank=False, default=0)
    metas = models.FloatField(blank=True, default=0)
    metas_pro = models.FloatField(blank=True, default=0)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-points"]

    def __str__(self):
        return f"{str(self.id_user)} - {self.points}"

    
class DoneList(models.Model):
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)

    metas = models.FloatField(blank=True, default=0)
    metas_pro = models.FloatField(blank=True, default=0)

    streak = models.BooleanField(blank=True)
    streak_count = models.IntegerField(blank=True, default=0)
    streak_max = models.IntegerField(blank=True, default=0)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_user)

    
class TaskBox(models.Model):
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
      
    metas = models.FloatField(blank=True, default=0)
    metas_pro = models.FloatField(blank=True, default=0)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.id_user)} - {str(self.edition)}"
    


