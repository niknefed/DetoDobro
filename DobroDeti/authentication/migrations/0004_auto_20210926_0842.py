# Generated by Django 3.2.7 on 2021-09-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_children_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_children',
            field=models.BooleanField(default=False, verbose_name='Воспитанник'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_director',
            field=models.BooleanField(default=False, verbose_name='Представитель'),
        ),
    ]
