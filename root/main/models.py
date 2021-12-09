from django.db import models
from datetime import date


class News(models.Model):
    """Новости на сайте"""
    title = models.CharField('Заголовок', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=300, default='')
    full_text = models.TextField('Новость', default='')
    poster = models.ImageField('Постер', upload_to="News/", default='')
    date = models.DateField('Дата', default=date.today)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
# class Prices(models.Model):
    
    
#     def __str__(self):
#         return self.status_name

#     class Meta:
#         verbose_name = 'Цена'
#         verbose_name_plural = 'Цены'
        
# class Gallery(models.Model):
    
    
#     def __str__(self):
#         return self.status_name

#     class Meta:
#         verbose_name = 'Изображение'
#         verbose_name_plural = 'Галерея'

# class Contacts(models.Model):
    
    
#     def __str__(self):
#         return self.status_name

#     class Meta:
#         verbose_name = 'Контакт'
#         verbose_name_plural = 'Контакты'