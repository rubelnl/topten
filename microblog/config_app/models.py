from django.db import models

# Create your models here.
class SiteConfig(models.Model):
    site_logo = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=100, default="")
    meta_title = models.CharField(max_length=200, default="")
    meta_description = models.TextField(default="")
    meta_keyword = models.TextField(default="")
    email = models.CharField(max_length=100, default="")
    facebook_url = models.CharField(max_length=300, default="")
    twitter_url = models.CharField(max_length=300, default="")
    google_plus_url = models.CharField(max_length=300, default="")
    youtube_url = models.CharField(max_length=300, default="")
    copyrights = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'

    def __str__(self):
        return self.title