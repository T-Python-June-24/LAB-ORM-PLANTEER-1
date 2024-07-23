from django.db import models

# Create your models here.

class model(models.Model):

    title = models.CharField(max_length=1024)
    description = models.TextField()
    benifit = models.TextField()
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")

