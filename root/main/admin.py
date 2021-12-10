from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Gallery, News, Partners


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'get_img', 'url', 'draft')
    list_display_links = ('title', )
    list_filter = ('title', 'date',)
    list_editable = ('draft',)
    actions = ['publish', 'unpublish']    
    fields = ('title', 'anons', 'text', 'date', 'image', 'get_img', 'url', 'draft')
    readonly_fields = ('get_img', )
    search_fields = ('title', )
    save_on_top = True
    save_as = True 
        
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

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'season', 'date', 'get_img')
    list_display_links = ('title', 'get_img')
    list_filter = ('title', 'season', 'date',)  
    search_fields = ('title', 'season')
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
    list_display = ('partner', 'get_img')
    list_display_links = ('partner', 'get_img')
    fields = ('partner', 'image', 'get_img')
    readonly_fields = ('get_img', )
    
    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="88px">')
        else:
            return 'нет картинки'
        
    get_img.short_description = 'Миниатюра'
    
admin.site.site_title = 'ENSOPARK'
admin.site.site_header = 'ENSOPARK'