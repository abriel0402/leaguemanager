# Generated by Django 4.2.1 on 2023-05-16 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
