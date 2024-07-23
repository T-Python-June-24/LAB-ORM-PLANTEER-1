from django.db import models



class Category(models.TextChoices):

    SUCCULENTS = 'Succulents', 'Succulents'
    CACTI = 'Cacti', 'Cacti'
    FLOWERS = 'Flowers', 'Flowering Plants'
    HERBS = 'Herbs', 'Herbs'
    SHRUBS = 'Shrubs', 'Shrubs'
    TREES = 'Trees', 'Trees'
    VINES_AND_CLIMBERS = 'Vines and Climbers', 'Vines and Climbers'
    FERNS = 'Ferns', 'Ferns'
    GRASSES = 'Grasses', 'Grasses'
    AQUATIC_PLANTS = 'Aquatic Plants', 'Aquatic Plants'
    BULBS = 'Bulbs', 'Bulbs'
    ORNAMENTAL_PLANTS = 'Ornamental Plants', 'Ornamental Plants'



class Plant(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    plant_image = models.ImageField(upload_to='plants/')
    category = models.CharField(
        max_length=50,
        choices=Category.choices,
        default=Category.SUCCULENTS,
    )
    is_edible = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

