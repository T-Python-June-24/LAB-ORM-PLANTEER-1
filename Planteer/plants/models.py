from django.db import models

# Create your models here.

class Plant(models.Model): 
  class Category(models.TextChoices):
    Herb = 'HRB', 'Herb'
    Trueree = 'TRE', 'Tree'
    Climber = 'CLB', 'Climber'
    Creeper = 'CRP', 'Creeper'


  name = models.CharField(max_length=512)
  about = models.TextField()
  used_for = models.TextField()
  image = models.ImageField(upload_to="images/")
  category = models.CharField(max_length=3, choices=Category.choices, default=Category.Herb)
  is_edible = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add=True)