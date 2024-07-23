# Generated by Django 5.0.7 on 2024-07-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0003_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='plants',
            name='rating',
            field=models.SmallIntegerField(choices=[(1, 'One Star'), (2, 'Two Star'), (3, 'Three Star'), (4, 'Four Star'), (5, 'Five Star')], default=3),
        ),
    ]
