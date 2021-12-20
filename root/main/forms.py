from django import forms
from django.forms import widgets

from .models import Order, Contacts


class AddPageForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'number']
        
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
                #    'email': forms.EmailInput(attrs={'class': 'form-control', 
                #                                    'placeholder': "Email (необязательно)",
                #                                    }),
        }
        
class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'description',]
        
        widgets = {'name': forms.TextInput(attrs={'id': "name", 
                                                  'type':"text", 
                                                  'class': 'form-control',
                                                  'placeholder': "Ваше имя",   
                                                  'name': "name", 
                                                  'required data-error': "Введите ваше имя",                                                                                                                          
                                                  }),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 
                                                   'placeholder': "Email",
                                                   'type': "text",
                                                   'id': "email",
                                                   'name': "email",
                                                   'required data-error': "Введите ваш email",
                                                   }),
                   'description': forms.Textarea(attrs={'class': "form-control",
                                                         'id': "message",
                                                         'placeholder': "Сообщение",
                                                         'rows': "7",
                                                        }),
        }