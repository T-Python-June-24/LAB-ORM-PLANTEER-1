from django.db import models

# Create your models here.

class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('tree', 'Tree'),
        ('shrub', 'Shrub'),
        ('flower', 'Flower'),
        ('herb', 'Herb'),
    ]

    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='media/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
