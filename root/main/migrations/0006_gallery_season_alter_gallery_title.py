# Generated by Django 4.0 on 2021-12-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_gallery_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='season',
            field=models.CharField(default='', max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Заголовок'),
        ),
    ]
