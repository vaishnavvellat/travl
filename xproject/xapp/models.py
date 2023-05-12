from django.db import models


# Create your models here.
class mud(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pic')
    desc = models.TextField()

    def __str__(self):
        return self.name


class axe(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pict')
    desc = models.TextField()

    def __str__(self):
        return self.name
