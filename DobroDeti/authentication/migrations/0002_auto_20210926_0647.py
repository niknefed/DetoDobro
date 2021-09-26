# Generated by Django 3.2.7 on 2021-09-26 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='age',
            field=models.CharField(blank=True, max_length=99, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='children',
            name='city',
            field=models.CharField(default=True, max_length=50, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='children',
            name='sex',
            field=models.CharField(blank=True, max_length=1, verbose_name='Пол'),
        ),
    ]
