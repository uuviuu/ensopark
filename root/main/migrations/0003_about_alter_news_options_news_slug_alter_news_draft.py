# Generated by Django 4.0 on 2021-12-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_news_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text_1', models.CharField(max_length=200, verbose_name='Основная информация')),
                ('text_2', models.TextField(verbose_name='Текст 1')),
                ('text_3', models.TextField(verbose_name='Текст 2')),
                ('image_1', models.ImageField(upload_to='about/', verbose_name='Изображение 1')),
                ('image_2', models.ImageField(upload_to='about/', verbose_name='Изображение 2')),
            ],
            options={
                'verbose_name': 'Информация',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='news',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Публикация'),
        ),
    ]