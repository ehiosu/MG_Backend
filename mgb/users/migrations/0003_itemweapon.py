# Generated by Django 4.2.1 on 2023-07-09 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_weapon_character_active_slots'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemWeapon',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.item')),
                ('damage_type', models.CharField(choices=[('Physical', 'Physical'), ('Fire', 'Fire'), ('Water', 'Water'), ('Wind', 'Wind'), ('Light', 'Light'), ('Dark', 'Dark')], max_length=10)),
                ('strength', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('dexterity', models.IntegerField()),
            ],
        ),
    ]
