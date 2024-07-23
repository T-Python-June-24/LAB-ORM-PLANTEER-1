from django.db import models

# Create your models here.
class Plant(models.Model):

    name = models.CharField(max_length=256)
    about = models.TextField()
    used_for = models.TextField()
    category = models.SmallIntegerField()
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    #file = models.FileField() #Any other file that is not image


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

  