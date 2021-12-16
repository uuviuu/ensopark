from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import About, Contacts, Gallery, News, Order, Partners, Prices

    
class IndexView(View):
    """Главная"""
    def get(self, request):
        return render(request, 'main/index.html')
    
class AboutView(View):
    """О нас"""
    def get(self, request):
        about = About.objects.all()
        return render(request, 'main/about.html', {'about': about})
    
class NewsView(ListView):
    """Новости"""
    def get(self, request):
        contact_list = News.objects.filter(draft=True)
        paginator = Paginator(contact_list, 3)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'main/news_list.html', {'page_obj': page_obj})
        
    # model = News
    # paginate_by = 3
    # template_name = 'main/news.html'
    # context_object_name = 'posts'
    
    # def get_queryset(self):
    #     return News.objects.filter(draft=False)
    
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return dict(list(context.items()))
    
class NewsDetailView(ListView):
    """Страница с новостью"""
    model = News
    
    def get(self, request):
        queryset = News.objects.filter(draft=False)
        return render(request, 'main/news.html', {'news': queryset})
    

    
class PriceView(View):
    """Цены"""
    def get(self, request):
        return render(request, 'main/price.html')
    
class GalleryView(View):
    """Галерея"""
    def get(self, request):
        return render(request, 'main/gallery.html')
    
class ContactsView(View):
    """Контакты"""
    def get(self, request):
        return render(request, 'main/contacts.html')