from django.db import models

class Plants(models.Model): # Inherent Model class to get ORM feature
    # name  CharField 
    # about  TextField
    # used_for  TextField
    # image    ImageField
    # category    CharField(TextChoices)
    # is_edible     BolleanField
    # created_at     DateTimeField(auto_now_add)

    
    name= models.CharField()
    about= models.TextField()
    used_for= models.TextField()
    image =  models.ImageField()
    category = models.CharField()
    is_edible = models.BooleanField()
    created_at = models.DateField()