# Generated by Django 5.0.7 on 2024-07-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagesPlanteer', '0002_rename_categore_plant_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
