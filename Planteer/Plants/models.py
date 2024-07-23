from django.db import models


class Plants(models.Model):
    
    class Category(models.TextChoices):
        INDOOR = 'Indoor', 'Indoor'
        OUTDOOR = 'Outdoor', 'Outdoor'
        FRUIT = 'Fruit', 'Fruit'
        VEGETABLE = 'Vegetable', 'Vegetable'
        HERB = 'Herb', 'Herb'
        FLOWER = 'Flower', 'Flower'
        TREE = 'Tree', 'Tree'
        SHRUB = 'Shrub', 'Shrub'

    class IntegerChoices(models.IntegerChoices):
        star1 = 1, 'One Star'
        star2 = 2,'Two Star'
        star3 = 3, 'Three Star'
        star4 = 4, 'Four Star'
        star5 = 5, 'Five Star'
        
    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    plant_image = models.ImageField(upload_to='images/', default='images/default.jpg')
    category = models.CharField(
        max_length=255,
        choices=Category.choices,
    )
   
    rating = models.SmallIntegerField(choices=IntegerChoices.choices, default=IntegerChoices.star3)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
