from django.contrib import admin
from blog_app.models import Category, Post, Item
# Register your models here.

# admin.site.site_header = 'TopTen admin'
# admin.site.site_title = 'TopTen admin'
# admin.site.site_url = '#'
# admin.site.index_title = 'TopTen administration'

admin.site.register(Category)


class ItemsInline(admin.TabularInline):
    model = Item
    exclude = ('votes', 'comments', 'mac_address')
    list_display = ('post_title', 'category', 'create_date')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ItemsInline]