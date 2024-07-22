# Generated by Django 5.0.7 on 2024-07-22 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.TextField(max_length=200)),
                ('used_for', models.TextField()),
                ('image', models.ImageField(default='images/default.png', upload_to='images')),
                ('categore', models.CharField(choices=[('Angiosperms', 'Angiosperms'), ('Pteridophytes', 'Pteridophytes'), ('Gymnosperms', 'Gymnosperms')], max_length=100)),
                ('is_edible', models.BooleanField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
