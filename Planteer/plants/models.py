from django.db import models

# Create your models here.
class Plant(models.Model):
    class CategoryChoices(models.TextChoices):
        TREES = "Trees", "Tree"
        FLOWERS = "Flowers", "Flower"
        HERBS = "Herbs", "Herb"
        FRUITS = "Fruits", "Fruit"
        VEGETABLES = "Vegetables", "Vegetable"

    name = models.CharField(max_length=256)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)