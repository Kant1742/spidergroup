# Generated by Django 3.1.2 on 2020-10-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='phone number'),
        ),
    ]
