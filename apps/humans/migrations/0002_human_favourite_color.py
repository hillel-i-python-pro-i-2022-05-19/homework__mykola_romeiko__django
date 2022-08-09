# Generated by Django 4.0.6 on 2022-08-08 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='favourite_color',
            field=models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('red', 'Red')], default='white', max_length=32, verbose_name='Favourite color'),
        ),
    ]