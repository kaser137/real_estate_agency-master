# Generated by Django 2.2.24 on 2023-03-13 22:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20230314_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
