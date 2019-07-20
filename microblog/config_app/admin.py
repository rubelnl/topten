from django.contrib import admin
from config_app.models import SiteConfig

# Register your models here.
@admin.register(SiteConfig)
class SiteConfig(admin.ModelAdmin):
    MAX_OBJECTS = 1

    def has_add_permission(self, request):
        if self.model.objects.count() >= self.MAX_OBJECTS:
            return False
        return super().has_add_permission(request)