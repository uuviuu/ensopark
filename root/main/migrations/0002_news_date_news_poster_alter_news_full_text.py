# Generated by Django 4.0 on 2021-12-09 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='news',
            name='poster',
            field=models.ImageField(default='', upload_to='News/', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='news',
            name='full_text',
            field=models.TextField(default='', verbose_name='Новость'),
        ),
    ]
