from django.db import models
from django.urls import reverse

from datetime import datetime

class About(models.Model):
    """О нас"""
    title = models.CharField("Заголовок", max_length=50)
    text_1 = models.CharField("Основная информация", blank=True, max_length=200,  help_text='Необязательное поле')
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
    title = models.CharField('Заголовок', max_length=50, help_text='Заголовок должен быть уникальным и автоматически пропишется в URL')
    anons = models.TextField('Анонс', max_length=200)
    text = models.TextField('Новость') 
    image = models.ImageField("Изображение", upload_to="news/", help_text='Добавьте изображение для отображения его на сайте')
    date = models.DateTimeField('Дата', default=datetime.now, help_text='По дате происходит сортировка новостей')
    draft = models.BooleanField("Публикация", default=True,)
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
    image = models.ImageField("Изображение", upload_to="gallery/", help_text='Для корректного отображения на сайте, добавляйте горизонтальные изображения соотношением 2 к 1')
    date = models.DateTimeField('Дата', default=datetime.now,  help_text='По дате происходит сортировка изображений')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Галерея'
        ordering = ["-date"]

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
    price_ad = models.CharField("Цена взрослый", blank=True, max_length=50, help_text='Необязательное поле')
    price_ch = models.CharField("Цена детский", blank=True, max_length=50, help_text='Необязательное поле')
    subscription = models.CharField("Цена абонемент", blank=True, max_length=50, help_text='Необязательное поле, заполняется в случае единого ценника, например на абонемент')
    # image = models.ImageField("Изображение", upload_to="prices/")
    image = models.FileField("Изображение", upload_to="prices/", ) # validators=[validate_svg]
    
    def __str__(self):
        return self.title 

    # def validate_svg(file, valid):
    #     if not is_image(file):
    #         raise ValidationError("File not svg")
    
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ["season"]
       
class Contacts(models.Model):
    """Контакты"""
    name = models.CharField("Имя", default='', max_length=50)
    email = models.EmailField('Email', max_length=100)
    description = models.TextField("Сообщение", default='')
    date = models.DateTimeField('Дата и время обращения', default=datetime.now)
    comment = models.TextField('Комментарий', default='', blank=True)
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ["-date"]

 
class Order(models.Model):
    """Запись с сайта"""
    date = models.DateTimeField('Дата и время заказа', default=datetime.now)
    name = models.CharField('Имя', max_length=100)
    number = models.CharField('Номер телефона', max_length=12)
    comment = models.TextField('Комментарий', default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись к инструкору'
        verbose_name_plural = 'Записи к инструктору'
        ordering = ["-date"]


# class Slider(models.Model):
#     img = models.ImageField(upload_to='slider/')
#     css = models.CharField(max_length=200,
#                                null=True,
#                                default='-',
#                                verbose_name='CSS класс')

#     class Meta:
#         verbose_name = 'Слайд'
#         verbose_name_plural = 'Слайды'   


