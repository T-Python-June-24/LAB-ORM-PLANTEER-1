from django.db import models

class Plants(models.Model): # Inherent Model class to get ORM feature 
    CATEGORY_CHOICES = [
        ('1', 'Fruit'),
        ('2', 'Vegetables'),
        ('3', 'Decorating tree'),
        ('4', 'Medicine'),
    ]   
    name= models.CharField(max_length=1024)
    about= models.TextField()
    used_for= models.TextField()
    image =  models.ImageField(upload_to="images/")
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    

    def __str__ (self) -> str:
        return self.name