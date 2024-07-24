from django.db import models
from django.utils.text import gettext_lazy
# Create your models here.

    # Plant info 


class Countries(models.Model):
    name=models.CharField(max_length=120,unique=True)
    def __str__(self) -> str:
        return self.name
class Plant (models.Model):
    class PlantChoices(models.TextChoices):
        TREE="Tree",gettext_lazy("Tree")
        FRUIT="Fruit",gettext_lazy("Fruit")
        VEGETABLES="Vegetables",gettext_lazy("Vegtables")

    name=models.CharField(max_length=1024)
    about=models.TextField()
    used_for=models.TextField()
    category=models.CharField(max_length=50,choices=PlantChoices.choices)
    image=models.ImageField(upload_to="images/" ,default="images/default_fruit.jpg")
    is_edible=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    countries=models.ManyToManyField(Countries)

    def __str__(self) -> str:
        return self.name

    # Contact Form
class Contact(models.Model):
    first_name=models.CharField(max_length=1024)
    last_name=models.CharField(max_length=1024)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
class Reivew(models.Model):
    plant=models.ForeignKey(Plant,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)



