# Generated by Django 3.2.3 on 2021-05-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_bikeorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycleorders',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bikeorders',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
