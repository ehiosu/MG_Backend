# Generated by Django 4.2.1 on 2023-07-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_itemweapon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
