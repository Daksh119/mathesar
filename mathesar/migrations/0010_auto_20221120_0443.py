# Generated by Django 3.1.14 on 2022-11-20 04:43

from django.db import migrations, models
from django.contrib.postgres.fields import ArrayField

class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0009_auto_20221123_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='TableSettings',
            name='column_order',
            field=ArrayField(models.IntegerField(), null=True, default=None)
        ),
    ]
