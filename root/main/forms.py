from datetime import datetime
from django import forms
from django.forms import widgets

from .models import Order


class AddPageForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'number', 'email']
        
        widgets = {'name': forms.TextInput(attrs={'id': "name", 
                                                  'type':"text", 
                                                  'class': 'form-control',
                                                  'placeholder': "Имя",                                                                                     
                                                  }),
                   'number': forms.TextInput(attrs={'id': "phone",
                                                   'type': "tel",
                                                   'class': 'form-control',                                                                                          
                                                   'pattern': "[0-9]{+}",
                                                   'required minlength': "12",
                                                   'maxlength': "12",
                                                   'name': "phone",
                                                   'placeholder': "Номер телефона",
                                                   }),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 
                                                   'placeholder': "Email (необязательно)",
                                                   }),
        }