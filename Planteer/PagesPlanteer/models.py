from django.db import models

# Create your models here.

class Plant(models.Model):
    plant_categore={
        "Angiosperms":"Angiosperms",
        "Pteridophytes":"Pteridophytes",
        "Gymnosperms":"Gymnosperms",
    }
    name = models.CharField(max_length=200)
    about = models.TextField(max_length=200)
    used_for  = models.TextField()
    image = models.ImageField(default='images/default.png' , upload_to='images/')
    category = models.CharField(choices=plant_categore , max_length=100)
    is_edible = models.BooleanField()
    created_at = models.DateField()
