from django.db import models

# Create your models here.
class Category(models.TextChoices):
    TREES = 'TREES', 'TREES'
    PLANT = 'PLANT', 'PLANT'
    Annuals = 'Annuals', 'Annuals'

class Plants(models.Model):

    name= models.CharField(max_length=1024)
    about= models.TextField()
    used_for= models.TextField(max_length=256,null=True)
    images= models.ImageField(upload_to="images/", default="images/default.jpg")
    category= models.CharField(max_length=9, choices=Category.choices,default='PLANT')
    is_edible= models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)


class contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()


