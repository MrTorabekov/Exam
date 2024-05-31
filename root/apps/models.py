from django.db import models

class Home(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    Tel_number = models.IntegerField()
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
