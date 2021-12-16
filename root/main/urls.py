from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('price/', views.PriceView.as_view(), name='price'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
]