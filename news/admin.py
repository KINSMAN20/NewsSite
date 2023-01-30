from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_at', 'get_photo', 'update_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'create_at', 'update_at')
    readonly_fields = ('get_photo', 'create_at', 'update_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'нет фото'

    get_photo.short_description = 'Фотография'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
