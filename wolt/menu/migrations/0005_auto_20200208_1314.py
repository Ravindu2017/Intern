# Generated by Django 2.2.7 on 2020-02-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200208_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='delivery_price',
            field=models.FloatField(),
        ),
    ]
