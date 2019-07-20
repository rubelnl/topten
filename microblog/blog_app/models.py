from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=150, default="")
    slug = AutoSlugField(populate_from='category_name', always_update=True, unique_with=['create_date__month'])
    description = models.TextField(default="")
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    create_by = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.SET_NULL)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        

    def __str__(self):
        return self.category_name


class Post(models.Model):
    post_title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='post_title', always_update=True, unique_with=['create_date__month'])
    long_desc = models.TextField(verbose_name="Long Description")
    post_img = models.ImageField(upload_to='images/', null=True)
    category = models.ManyToManyField("Category")
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    create_by = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.SET_NULL)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.post_title


class Item(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, blank=True, null=True)
    item_title = models.CharField(max_length=250, verbose_name="Item Name")
    short_desc = models.TextField(verbose_name="Short Description")
    item_img = models.ImageField(upload_to='images/', null=True, blank=True)
    comments = models.ManyToManyField(User, related_name='comments', blank=True)
    mac_address = models.TextField(null=True)
    is_approved = models.BooleanField(editable=True, default=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    create_by = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.SET_NULL)
    update_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.item_title


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    voted_by = models.IntegerField(null=True, blank=True)
    mac_address = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

