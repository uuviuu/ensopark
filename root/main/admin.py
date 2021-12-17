from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import About, Contacts, Gallery, News, Order, Partners, Prices

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
    list_display = ('title', 'season', 'price', 'get_img')
    list_display_links = ('title', 'get_img')
    list_filter = ('title', 'season', 'price') 
    fields = ('title', 'season', 'description', 'price', 'image', 'get_img')
    readonly_fields = ('get_img', )
    
    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="88px">')
        else:
            return 'нет картинки'
        
    get_img.short_description = 'Миниатюра'

    
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'season', 'date', 'get_img')
    list_display_links = ('title', 'get_img')
    list_filter = ('title', 'season', 'date') 
    fields = ('title', 'season', 'date', 'image', 'get_img')
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
    list_display = ('name', 'number', 'email', 'data', 'comment')
    list_display_links = ('name', 'number', 'email')
    list_filter = ('data', 'name', 'number', 'email')
    list_per_page = 10
    list_max_show = 100
    fields = ('name', 'number', 'email', 'data', 'comment')
    readonly_fields = ('data',)

admin.site.register(Contacts)

admin.site.site_title = 'ENSOPARK'
admin.site.site_header = 'ENSOPARK'