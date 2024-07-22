from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now=True)