# Generated by Django 2.2.2 on 2019-07-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_remove_post_short_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='mac_address',
            field=models.TextField(null=True),
        ),
    ]
