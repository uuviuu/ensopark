from django.db import models
from django.urls import reverse

from datetime import date


class News(models.Model):
    """Новости на сайте"""
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Анонс', max_length=300)
    text = models.TextField('Новость')
    image = models.ImageField("Изображение", upload_to="news/")
    date = models.DateField('Дата', default=date.today)
    url = models.SlugField(max_length=130, unique=True,)
    draft = models.BooleanField("Черновик", default=False)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Gallery(models.Model):
    """Галерея"""
    title = models.CharField("Заголовок", max_length=50)
    season = models.CharField("Сезон", max_length=50)
    image = models.ImageField("Изображение", upload_to="gallery/")
    date = models.DateField('Дата', default=date.today)
    
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Галерея'

class Partners(models.Model):
    """Партнеры"""
    partner = models.CharField("Партнер", max_length=100)
    image = models.ImageField("Изображение", upload_to="partners/")
    
    def __str__(self):
        return self.partner

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'   
        
class Prices(models.Model):
    """Цены на летнике виды услуг"""
    title = models.CharField("Услуга", max_length=50)
    season = models.CharField("Сезон", max_length=50)
    description = models.TextField('Описание')
    price = models.CharField("Цена", max_length=50)
    image = models.ImageField("Изображение", upload_to="prices/")
    
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
       
class Contacts(models.Model):
    """Контактная информация"""
    email = models.EmailField('Email', max_length=100)
    number = models.CharField("Номер", max_length=12)
    address = models.CharField("Адрес", max_length=100)
    description = models.TextField("Описание")
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'      


        


