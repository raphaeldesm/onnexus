from django.db import models

# Create your models here.
class Post(models.Model):
    profile = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/posts/%Y/%m/%d', null=False, blank=False)
    favorites = models.IntegerField()
    views = models.IntegerField()

    def __str__(self):
        return self.username