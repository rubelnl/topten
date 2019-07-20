from django.shortcuts import render
from blog_app.models import Post
from config_app.models import SiteConfig


def sidebar_post(request):
    featured = Post.objects.filter(category__slug='featured').order_by("-create_date")[:5]
    popluar = Post.objects.all().order_by("-create_date")[:5]
    recent = Post.objects.all().order_by("-create_date")[:5]
    context = {
        'featured_posts': featured,
        'popluar_posts': popluar,
        'recent_posts': recent
    }
    return context


def site_setting(request):
    try:
        setting = SiteConfig.objects.all().order_by('-id')[0]
    except:
        setting = None

    context = {'setting': setting}
    return context
