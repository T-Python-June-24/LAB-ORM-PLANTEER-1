from django.db import models

class Category(models.TextChoices):
    INDOOR = 'Indoor', 'Indoor'
    OUTDOOR = 'Outdoor', 'Outdoor'
    FRUIT = 'Fruit', 'Fruit'
    VEGETABLE = 'Vegetable', 'Vegetable'
    HERB = 'Herb', 'Herb'
    FLOWER = 'Flower', 'Flower'
    TREE = 'Tree', 'Tree'
    SHRUB = 'Shrub', 'Shrub'

class Plants(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    plant_image = models.ImageField(upload_to='images/', default='images/default.jpg')
    category = models.CharField(
        max_length=255,
        choices=Category.choices,
    )
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
