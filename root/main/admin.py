from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')



admin.site.site_title = 'INIKOO'
admin.site.site_header = 'INIKOO'