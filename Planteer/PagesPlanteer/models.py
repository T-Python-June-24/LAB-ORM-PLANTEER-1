from django.db import models

# Create your models here.

def plant():
    plant_categore={
        "Angiosperms":"Angiosperms",
        "Pteridophytes":"Pteridophytes",
        "Gymnosperms":"Gymnosperms",
    }
    name = models.CharField(max_length=200)
    about = models.TextField(max_length=200)
    used_for  = models.TextField()
    image = models.ImageField(default='images/default.png' , upload_to='images')
    categore = models.CharField(choices=plant_categore)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField()
