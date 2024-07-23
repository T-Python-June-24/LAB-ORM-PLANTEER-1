from django.db import models


class Plant(models.Model):

    class categoryChoices(models.TextChoices):

        CATEGORY1 = "fruit" , "Fruit"
        CATEGORY2 = "tree" , "Tree"
        CATEGORY3 = "vegetables" , "Vegetables"

    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    category = category = models.CharField(max_length=1024,choices=categoryChoices.choices)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")