# Generated by Django 4.0 on 2022-01-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prices',
            name='image_png',
            field=models.ImageField(blank=True, help_text='Необязательно', upload_to='prices/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='prices',
            name='image',
            field=models.FileField(upload_to='prices/', verbose_name='Иконка'),
        ),
    ]