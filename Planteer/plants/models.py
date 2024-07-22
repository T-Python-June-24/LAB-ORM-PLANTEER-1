from django.db import models


class plant(models.Model):
    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    category = category = models.CharField(max_length=100, choices=[('fruit', 'Fruit'), ('tree', 'Tree'), ('vegetables', 'Vegetables')])
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")