from django.db import models
from django.urls import reverse

from datetime import date, datetime

class About(models.Model):
    """О нас"""
    title = models.CharField("Заголовок", max_length=50)
    text_1 = models.CharField("Основная информация", max_length=200)
    text_2 = models.TextField("Текст 1")
    text_3 = models.TextField("Текст 2")
    image_1 = models.ImageField("Изображение 1", upload_to="about/")
    image_2 = models.ImageField("Изображение 2", upload_to="about/")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'О нас'   

class News(models.Model):
    """Новости на сайте"""
    title = models.CharField('Заголовок', max_length=50, help_text='Заголовок должен быть уникальныи, он будет служить для вас ориентиром в новостях и автоматически пропишется в URL')
    anons = models.CharField('Анонс', max_length=300)
    text = models.TextField('Новость')
    image = models.ImageField("Изображение", upload_to="news/",  help_text='Для корректного отображения на сайте, добавляйте горизонтальные изображения соотношением 2 к 1')
    date = models.DateField('Дата', default=date.today)
    draft = models.BooleanField("Публикация", default=True)
    slug = models.SlugField("URL", max_length=50, unique=True, db_index=True, default='', help_text='URL для новости должен быть уникальным')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ["-date"]

class Gallery(models.Model):
    """Галерея"""
    title = models.CharField("Заголовок", max_length=50, blank=True)
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
    adress = models.TextField('Ссылка на партнера', default='')
    
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

 
class Order(models.Model):
    """Заявки с сайта"""
    data = models.DateTimeField('Дата и время заказа', default=datetime.now)
    name = models.CharField('Имя', max_length=100)
    number = models.CharField('Номер телефона', max_length=12)
    email = models.EmailField('Email', max_length=100, blank=True)
    comment = models.TextField('Комментарий', default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


        


