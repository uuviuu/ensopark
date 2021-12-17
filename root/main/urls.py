from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path("news/<slug:slug>/", views.newsdetail, name="news_detail"),
    path('price/', views.PriceView.as_view(), name='price'),
    path('gallery/', views.gallery, name='gallery'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
]