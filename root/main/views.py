from django.core.paginator import Paginator
from django.shortcuts import redirect, render
# from django.views.generic import ListView, DetailView
# from django.views.generic.base import View

from .models import About, Gallery, News, Partners, Prices
from .forms import *

def index(request):
    """Главная"""
    contact_list = News.objects.filter(draft=True)
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    prices = Prices.objects.all()
    partners = Partners.objects.all()
    gallery = Gallery.objects.order_by('-date')[:12]

    if request.method == 'POST':
        form = AddPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddPageForm()                  

    return render(request, 'main/index.html', { 'form': form, 'page_obj': page_obj, 'partners': partners, 'gallery': gallery, 'prices': prices })


def about(request):
    """О нас"""
    about = About.objects.all()

    if request.method == 'POST':
        form = AddPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = AddPageForm()

    return render(request, 'main/about.html', {'about': about, 'form': form})


def news(request):
    """Новости"""

    if request.method == 'POST':
        form = AddPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = AddPageForm()

    contact_list = News.objects.filter(draft=True)
    paginator = Paginator(contact_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/news_list.html', {'page_obj': page_obj, 'form': form})


def newsdetail(request, slug):
    """Страница с новостью"""

    if request.method == 'POST':
        form = AddPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_detail')
    else:
        form = AddPageForm()

    news = News.objects.filter(draft=True).get(slug=slug)
    return render(request, 'main/news_detail.html', {'news': news, 'form': form})


def gallery(request):
    """Галерея"""
    gallery = Gallery.objects.order_by('-date')

    if request.method == 'POST':
        form = AddPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = AddPageForm()

    return render(request, 'main/gallery.html', {'gallery': gallery, 'form': form})


def prices(request):
    """Цены"""

    prices = Prices.objects.all()

    if request.method == 'POST':
        form = AddPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prices')
    else:
        form = AddPageForm()

    return render(request, 'main/prices.html', {'prices': prices, 'form': form})



def contacts(request):
    """Контакты"""

    if request.method == 'POST':
        form = AddPageForm(request.POST)
        contacts = ContactsForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('contacts')
        
        if contacts.is_valid():
            contacts.save()
            return redirect('contacts')
    else:
        form = AddPageForm()
        contacts = ContactsForm
    
    return render(request, 'main/contacts.html', {'contacts': contacts, 'form': form})


# class IndexView(View):
#     """Главная"""
#     def get(self, request):
#         if request.method == 'POST':
#             form = AddPageForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('index')
#         else:
#             form = AddPageForm()
#         return render(request, 'main/index.html', {'form': form})

# class AboutView(View):
#     """О нас"""
#     def get(self, request):
#         about = About.objects.all()
#         if request.method == 'POST':
#             form = AddPageForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('about')
#         else:
#             form = AddPageForm()
#         return render(request, 'main/about.html', {'about': about, 'form': form})

# class NewsView(ListView):
#     """Новости"""
#     def get(self, request):

#         if request.method == 'POST':
#             form = AddPageForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('news')
#         else:
#             form = AddPageForm()

#         contact_list = News.objects.filter(draft=True)
#         paginator = Paginator(contact_list, 3)

#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         return render(request, 'main/news_list.html', {'page_obj': page_obj, 'form': form})

# class NewsDetailView(View):
#     """Страница с новостью"""
#     model = News
#     slug_field = "slug"

#     def get(self, request, slug):
#         news = News.objects.filter(draft=True).get(slug=slug)
#         return render(request, 'main/news_detail.html', {'news': news})

# class GalleryView(View):
#     """Галерея"""
#     def get(self, request):
#         gallery = Gallery.objects.all()
#         return render(request, 'main/gallery.html', {'gallery': gallery, 'form': form})

# class PriceView(View):

#     def get(self, request):
#         return render(request, 'main/price.html')