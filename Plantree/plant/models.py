from django.db import models

class Plants(models.Model): # Inherent Model class to get ORM feature    
    name= models.CharField(max_length=1024)
    about= models.TextField()
    used_for= models.TextField()
    image =  models.ImageField()
    category = models.CharField(max_length=255)
    is_edible = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)