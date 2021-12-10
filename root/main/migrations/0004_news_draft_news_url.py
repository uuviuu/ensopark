# Generated by Django 4.0 on 2021-12-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_gallery_rename_full_text_news_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Черновик'),
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.SlugField(default='', max_length=130, unique=True),
        ),
    ]