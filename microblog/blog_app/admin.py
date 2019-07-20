from django.contrib import admin
from .models import Category, Post, Item, SiteSetting
# Register your models here.

# admin.site.site_header = 'TopTen admin'
# admin.site.site_title = 'TopTen admin'
# admin.site.site_url = '#'
# admin.site.index_title = 'TopTen administration'

admin.site.register(Category)


@admin.register(SiteSetting)
class SiteSetting(admin.ModelAdmin):
    MAX_OBJECTS = 1

    def has_add_permission(self, request):
        if self.model.objects.count() >= self.MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


class ItemsInline(admin.TabularInline):
    model = Item
    exclude = ('votes', 'comments', 'mac_address')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ItemsInline]
