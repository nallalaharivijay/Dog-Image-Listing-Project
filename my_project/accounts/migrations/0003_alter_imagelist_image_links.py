# Generated by Django 5.1 on 2024-11-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_imagelist_image_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelist',
            name='image_links',
            field=models.JSONField(),
        ),
    ]
