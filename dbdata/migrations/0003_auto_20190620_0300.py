# Generated by Django 2.2.2 on 2019-06-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbdata', '0002_pg_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pg',
            name='img',
            field=models.ImageField(default='property-img-default.gif', upload_to='pics'),
        ),
    ]
