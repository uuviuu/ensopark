from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from .models import About, Contacts, Gallery, News, Order, Partners, Prices

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(label='Новость', widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'
        
class PriceAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Prices
        fields = '__all__'
        
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):   
    list_display = ('title',)
    list_display_links = ('title',)
    fields = ('title', 'text_1', 'text_2', 'text_3', 'image_1', 'image_2', 'get_img', 'get_img_2')
    readonly_fields = ('get_img', 'get_img_2')
    
    def get_img(self, obj):
        if obj.image_1:
            return mark_safe(f'<img src="{obj.image_1.url}" width="88px">')
        else:
            return 'нет картинки'
        
    def get_img_2(self, obj):
        if obj.image_2:
            return mark_safe(f'<img src="{obj.image_2.url}" width="88px">')
        else:
            return 'нет картинки'
        
    get_img.short_description = 'Миниатюра 1'
    get_img_2.short_description = 'Миниатюра 2'
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'get_img', 'draft')
    list_display_links = ('title', )
    list_filter = ('date', 'draft')
    list_editable = ('draft',)
    form = NewsAdminForm
    actions = ['publish', 'unpublish']    
    fields = ('title', 'anons', 'text', 'date', 'image', 'get_img', 'draft', 'slug')
    readonly_fields = ('get_img', )
    save_on_top = True
    save_as = True 
    prepopulated_fields =  {"slug": ("title",)}
    
    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="88px">')
        else:
            return 'нет картинки'
    
    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{ row_update } записи были обновлены'
        self.message_user(request, f'{ message_bit }') 
        
    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{ row_update } записи были обновлены'
        self.message_user(request, f'{ message_bit }')    
        
    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change', )    
    
    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change', )  
    
    get_img.short_description = 'Миниатюра'    
    
@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):   
    list_display = ('title', 'season', 'price_ad', 'price_ch', 'subscription', 'get_img')
    list_display_links = ('title', 'get_img', 'price_ad', 'price_ch', 'subscription', 'get_img')
    list_filter = ('title', 'season', ) 
    fields = ('title', 'description', 'season', 'price_ad', 'price_ch', 'subscription', 'image_png', 'image', 'get_img', "slug")
    form = PriceAdminForm
    readonly_fields = ('get_img', )
    prepopulated_fields =  {"slug": ("title",)}
    
    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="88px">')
        if obj.image_png:
            return mark_safe(f'<img src="{obj.image_png.url}" width="200px">')
        else:
            return 'нет картинки'
        
  
        
    get_img.short_description = 'Миниатюра'

    
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('get_img', 'date')
    list_display_links = ('get_img',)
    list_filter = ('date',) 
    fields = ('date', 'image', 'get_img')
    readonly_fields = ('get_img', )
    
    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="88px">')
        else:
            return 'нет картинки'
        
    get_img.short_description = 'Миниатюра'

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('partner', 'adress', 'get_img')
    list_display_links = ('partner', 'get_img')
    fields = ('partner', 'adress', 'image', 'get_img')
    readonly_fields = ('get_img',)
    
    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="88px">')
        else:
            return 'нет картинки'
        
    get_img.short_description = 'Миниатюра'
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'date', 'comment')
    list_display_links = ('name', 'number', )
    list_filter = ('date', 'name', 'number', )
    list_per_page = 10
    list_max_show = 100
    fields = ('name', 'number', 'date', 'comment')
    readonly_fields = ('date',)

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'comment')
    list_display_links = ('name', 'email', )
    list_filter = ('date', 'name',)
    list_per_page = 10
    list_max_show = 100
    fields = ('name', 'email', 'description', 'date', 'comment')
    readonly_fields = ('date',)
    
# @admin.register(Slider)
# class SliderAdmin(admin.ModelAdmin):
#     list_display = ('get_img', 'css',)
#     list_display_links = ('get_img',)
#     fields = ('img', 'get_img', 'css',)
#     list_editable = ('css', )
#     readonly_fields = ('get_img', )

#     def get_img(self, obj):
#         if obj.img:
#             return mark_safe(f'<img src="{obj.img.url}" width="88px">')
#         else:
#             return 'нет картинки'

#     get_img.short_description = 'Миниатюра'
    
admin.site.site_title = 'ENSOPARK'
admin.site.site_header = 'ENSOPARK'
admin.site.index_title = 'ENSOPARK'
