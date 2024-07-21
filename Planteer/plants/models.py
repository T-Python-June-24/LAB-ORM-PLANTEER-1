from django.db import models

# Create your models here.

class Plant(models.Model):

    name = models.CharField(max_length=256)
    about = models.TextField()
    used_for = models.TextField()
    image=models.ImageField(upload_to="images/",default="images/default.jpg")
    category=models.CharField(max_length=256)
    is_edible=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
# name ,about,used_for,image,category,is_edible,created_at
